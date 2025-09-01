import axios from 'axios'

// Configurazione base per le chiamate API
const API_BASE_URL = 'http://localhost:8000'

const api = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  }
})

// Interceptor per gestire errori globalmente
api.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error('API Error:', error)
    return Promise.reject(error)
  }
)

// Servizi API
export const apiService = {
  // Ottieni impostazioni del sito
  async getSiteSettings() {
    try {
      const response = await api.get('/api/settings/')
      return response.data
    } catch (error) {
      console.error('Error fetching site settings:', error)
      throw error
    }
  },

  // Ottieni lista servizi
  async getServices() {
    try {
      const response = await api.get('/api/services/')
      return response.data
    } catch (error) {
      console.error('Error fetching services:', error)
      throw error
    }
  },

  // Ottieni lista progetti
  async getProjects() {
    try {
      const response = await api.get('/api/projects/')
      return response.data
    } catch (error) {
      console.error('Error fetching projects:', error)
      throw error
    }
  },

  // Ottieni progetti in evidenza
  async getFeaturedProjects() {
    try {
      const response = await api.get('/api/projects/featured/')
      return response.data
    } catch (error) {
      console.error('Error fetching featured projects:', error)
      throw error
    }
  },

  // Invia messaggio di contatto
  async sendContact(contactData) {
    try {
      const response = await api.post('/api/contact/', contactData)
      return response.data
    } catch (error) {
      console.error('Error sending contact:', error)
      throw error
    }
  }
}

export default api
