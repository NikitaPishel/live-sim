import axios from 'axios';
import { computed, ref } from 'vue'
import { defineStore } from 'pinia'

const STORE_NAME = 'simData'
const CHANNEL_LIST_ENDPOINT = 'http://127.0.0.1'

export const useChannelsStore = defineStore(STORE_NAME, () => {
  const jsonData = ref({});

  const simStat = computed(() => jsonData.value.data);

  async function loadData() {
    try {
      const response = await axios.get(CHANNEL_LIST_ENDPOINT)
      jsonData.value = response.data
    } catch(e) {
      console.error('Error fetching the JSON file:', e);
    }
  };
  
  loadData();
  
  return {
    simStat,
  }
})