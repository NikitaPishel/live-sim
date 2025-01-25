import axios from 'axios';
import { computed, ref } from 'vue'
import { defineStore } from 'pinia'

const STORE_NAME = 'simData'
const BASE_URL = 'http://127.0.0.1:5000'

export const useChannelsStore = defineStore(STORE_NAME, () => {
  const jsonData = ref({});

  const simStat = computed(() => jsonData.value.data);
  
  // fetch status from the server
  async function getStatus() {
      try {
          const response = await axios.get(`${BASE_URL}/dev/status`);
          console.log('Server Status:', response.data);
      } catch (error) {
          console.error('Error fetching status:', error);
      }
  }

  async function loadStat() {
    try {
      const response = await axios.get(BASE_URL)
      jsonData.value = response.data
    } catch(e) {
      console.error('Error fetching the JSON file:', e);
    }
  };
  
  loadStat();
  
  return {
    simStat,
  }
})