<!-- Popup menu with genomes -->

<script setup>
import { computed } from 'vue';
import { usePopupStore } from '@/stores/popupStore.js';
import popupControl from '@/components/popups/popupControl.vue';

const popupStore = usePopupStore()
const passedNum = computed (() => popupStore.popupsDisplay.passedNum)
</script>

<template>
<popupControl v-if="passedNum" :displayState="'passedNum'">
    <div>
        <h1>Amount of passed agents</h1>
        <p>{{ passedNum }}</p>
    </div>
</popupControl>
</template>

<style>
</style>