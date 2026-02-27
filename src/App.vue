<script setup>
import Navbar from './components/Navbar.vue';
import Hero from './components/Hero.vue';
import LiveTicker from './components/LiveTicker.vue';
import Features from './components/Features.vue';
import Footer from './components/Footer.vue';
</script>

<template>
  <main class="min-h-screen bg-black text-white overflow-x-hidden">
    <!-- Navbar -->
    <Navbar />
    
    <!-- Hero Section -->
    <Hero />
    
    <!-- Live Ticker -->
    <LiveTicker />
    
    <!-- Features / Creator Grid -->
    <section class="relative">
      <Features />
    </section>
    
    <!-- Footer -->
    <Footer />
  </main>
</template>
