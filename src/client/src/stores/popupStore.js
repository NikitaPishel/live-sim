import axios from 'axios';
import { computed, ref } from 'vue'
import { defineStore } from 'pinia'

const STORE_NAME = 'popupData'
const BASE_URL = 'http://127.0.0.1:5000'

export const usePopupStore = defineStore(STORE_NAME, () => {

  const popupsDisplay = ref({
    genome: true,
  });

  function switchPopup (trigger) {
    console.log(`switching state ${trigger} from ${popupsDisplay.value[trigger]} to ${!popupsDisplay.value[trigger]}`)
    popupsDisplay.value[trigger] = !popupsDisplay.value[trigger]
  };
  
  return {
    popupsDisplay,
    switchPopup,
  }
})