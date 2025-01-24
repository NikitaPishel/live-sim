<script setup>
  import { ref } from 'vue';
  import { RouterView } from 'vue-router'

  import axios from 'axios';

const BASE_URL = 'http://localhost:5000';

// fetch status from the server
async function getStatus() {
    try {
        const response = await axios.get(`${BASE_URL}/dev/status`);
        console.log('Server Status:', response.data);
    } catch (error) {
        console.error('Error fetching status:', error);
    }
}

getStatus();

</script>

<template>
  <div class="page">
    <div class="header">
      <div>Menu 1</div>
      <div>Menu 2</div>
    </div>
    <div class="content">
      <RouterView />
    </div>
  </div>
  
</template>

<script>

</script>