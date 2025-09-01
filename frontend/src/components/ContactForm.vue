<template>
  <div class="contact-form">
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label for="name">Nome *</label>
        <input
          id="name"
          v-model="form.name"
          type="text"
          required
          :disabled="loading"
          placeholder="Il tuo nome"
        />
      </div>
      
      <div class="form-group">
        <label for="email">Email *</label>
        <input
          id="email"
          v-model="form.email"
          type="email"
          required
          :disabled="loading"
          placeholder="la-tua-email@esempio.com"
        />
      </div>
      
      <div class="form-group">
        <label for="company">Azienda</label>
        <input
          id="company"
          v-model="form.company"
          type="text"
          :disabled="loading"
          placeholder="Nome della tua azienda (opzionale)"
        />
      </div>
      
      <div class="form-group">
        <label for="subject">Oggetto *</label>
        <input
          id="subject"
          v-model="form.subject"
          type="text"
          required
          :disabled="loading"
          placeholder="Di cosa vorresti parlare?"
        />
      </div>
      
      <div class="form-group">
        <label for="message">Messaggio *</label>
        <textarea
          id="message"
          v-model="form.message"
          required
          :disabled="loading"
          placeholder="Raccontaci del tuo progetto, delle tue esigenze o delle sfide che stai affrontando..."
        ></textarea>
      </div>
      
      <div class="form-group">
        <button 
          type="submit" 
          class="btn primary"
          :disabled="loading || !isFormValid"
        >
          {{ loading ? 'Invio in corso...' : 'Invia messaggio' }}
        </button>
      </div>
      
      <!-- Messaggi di feedback -->
      <div v-if="successMessage" class="message success">
        {{ successMessage }}
      </div>
      
      <div v-if="errorMessage" class="message error">
        {{ errorMessage }}
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { apiService } from '../services/api.js'

const loading = ref(false)
const successMessage = ref('')
const errorMessage = ref('')

const form = ref({
  name: '',
  email: '',
  company: '',
  subject: '',
  message: ''
})

// Validazione form
const isFormValid = computed(() => {
  return form.value.name.trim() && 
         form.value.email.trim() && 
         form.value.subject.trim() && 
         form.value.message.trim()
})

// Invio form
const submitForm = async () => {
  if (!isFormValid.value) return
  
  loading.value = true
  successMessage.value = ''
  errorMessage.value = ''
  
  try {
    const response = await apiService.sendContact({
      name: form.value.name.trim(),
      email: form.value.email.trim(),
      company: form.value.company.trim(),
      subject: form.value.subject.trim(),
      message: form.value.message.trim()
    })
    
    successMessage.value = response.message || 'Messaggio inviato con successo! Ti risponderemo presto.'
    
    // Reset form
    form.value = {
      name: '',
      email: '',
      company: '',
      subject: '',
      message: ''
    }
    
  } catch (error) {
    console.error('Error sending contact:', error)
    errorMessage.value = error.response?.data?.message || 'Errore nell\'invio del messaggio. Riprova più tardi.'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.message {
  padding: 12px 16px;
  border-radius: 8px;
  margin-top: 16px;
  font-size: 14px;
}

.message.success {
  background-color: #d4edda;
  color: #155724;
  border: 1px solid #c3e6cb;
}

.message.error {
  background-color: #f8d7da;
  color: #721c24;
  border: 1px solid #f5c6cb;
}

button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

button:disabled:hover {
  transform: none;
  box-shadow: none;
}
</style>
