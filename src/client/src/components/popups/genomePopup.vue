<!-- Popup menu with genomes -->

<script setup>
import { computed } from 'vue';
import { usePopupStore } from '@/stores/popupStore.js';
import popupControl from '@/components/popups/popupControl.vue';

const popupStore = usePopupStore()
const genome = computed (() => popupStore.popupsDisplay.genome)
</script>

<template>
<popupControl v-if="genome" :displayState="'genome'">
    <div>
        <h1>Genome</h1>
        <p>{{ genome }}</p>
    </div>
</popupControl>
</template>

<style>
</style>