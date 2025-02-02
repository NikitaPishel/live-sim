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
    <div class="dataCell">
        <h3 class="panelHead">Genomes</h3>
    </div>
    
    <div class="dataCell">
        <h3 class="sectnHead">Table</h3>
        <div class="sectnContent">
        </div>
    </div>
</popupControl>
</template>

<style>
</style>