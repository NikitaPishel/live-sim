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

//getStatus();

</script>

<template>
  <div class="page">
    <div class="header">
      <div class="navigation">Menu 1</div>
      <div class="navigation">Menu 2</div>
    </div>
    <div class="content">
      <RouterView />
    </div>
  </div>
  
</template>

<style>
.navigation {
  margin-left: 0.3%;
  margin-right: 0.3%;
}

.page {
  background-color: #d5c4b7;
  height: 100%;
  width: 100%;
  margin: 0;
  padding: 0;
}

.header {
  background-color: #d5c4b7;
  
  border-color: #3d3d3d;
  border-bottom-width: 5px;
  
  margin: 0;
  padding: 12px;

  height: 20%;

  display: flex;
}

.content {
  background-color: #efe3da;
  margin: 0%;
  padding: 0%;

  height: 80%;
}
</style>