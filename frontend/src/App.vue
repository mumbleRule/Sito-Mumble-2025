<script setup>
import AppHeader from './components/AppHeader.vue'
import AppFooter from './components/AppFooter.vue'
</script>

<template>
  <div id="app">
    <AppHeader />

    <main>
      <router-view />
    </main>

    <AppFooter />
  </div>
</template>

<style>
/* Import degli stili globali */
@import './assets/styles/main.css';
</style>
