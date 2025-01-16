<script setup>
  import { ref } from 'vue';
  import chartComponent from './components/ChartComponent.vue';

</script>
<template>

  <h1>Hello world!</h1>

  <chartComponent></chartComponent>

</template>

<script>
import axios from 'axios';

const BASE_URL = 'http://localhost:5000';

// fetch status from the server
async function getStatus() {
    try {
        const response = await axios.get(`${BASE_URL}/api/status`);
        console.log('Server Status:', response.data);
    } catch (error) {
        console.error('Error fetching status:', error);
    }
}

getStatus();
</script>