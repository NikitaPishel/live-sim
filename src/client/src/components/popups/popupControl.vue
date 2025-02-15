<script setup>
import { computed } from 'vue'
import { usePopupStore } from '@/stores/popupStore.js';

const popupStore = usePopupStore()
const props = defineProps(['displayState'])

const closePopup = () => {
    popupStore.switchPopup(props.displayState)
}
</script>

<template>
    <div class="popupShade">
        <div class="content" id="popupData">
            <slot />

            <button class="popupButton" @click="() => closePopup()">
                Close
            </button>
        </div>
    </div>
</template>

<style scoped lang="scss">
.popupShade {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(0, 0, 0, 0.3);
    
    display: flex;
    align-items: center;
    justify-content: center;
}

#popupData {
    margin: 0;
    padding: 4%;
}

.dark {
    .popupShade {
        background-color: rgba(255, 255, 255, 0.2);
    }
}
</style>