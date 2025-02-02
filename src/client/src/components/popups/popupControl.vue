<script>
import { usePopupStore } from '@/stores/popupStore.js';

const popupStore = usePopupStore()

const switchPopup = popupStore.switchPopup

export default {
    setup () {
        props: ['displayState']
    }
}
</script>

<template>
    <div class="popupShade">
        <div class="content" id="popupData">
            <slot />

            <button class="popupButton" @click="() => switchPopup('displayState')">
                Close
            </button>
        </div>
    </div>
</template>

<style scoped>
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
    background-color: #fef4ee;

    margin: 0;
    padding: 4%;
}
</style>