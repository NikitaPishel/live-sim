<!-- Popup menu with percentage of survived agents -->

<script setup>
import { computed } from 'vue';
import { usePopupStore } from '@/stores/popupStore.js';
import popupControl from '@/components/popups/popupControl.vue';

const popupStore = usePopupStore()
const surviv = computed (() => popupStore.popupsDisplay.surviv)
</script>

<template>
<popupControl v-if="surviv" :displayState="'surviv'">
    <div>
        <h1>Survivability percentage</h1>
        <p>{{ surviv }}</p>
    </div>
</popupControl>
</template>

<style>
</style>