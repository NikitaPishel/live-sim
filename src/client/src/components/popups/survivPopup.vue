<!-- Popup menu with percentage of survived agents -->

<script setup>
import { computed } from 'vue';
import { usePopupStore } from '@/stores/popupStore.js';
import popupControl from '@/components/popups/popupControl.vue';
import leftBarBox from '@/components/dataBoxes/leftBarBox.vue'
import ChartComponent from '@/components/charts/ChartComponent.vue';

const popupStore = usePopupStore()
const surviv = computed (() => popupStore.popupsDisplay.surviv)
</script>

<template>
    <popupControl v-if="surviv" :displayState="'surviv'">
        <div class="dataCell">
            <h3 class="panelHead">Survivability percentage</h3>
        </div>
    
        <div class="dataCell">  
            <h3 class="sectnHead"></h3>
            <div class="sectnContent">
                <leftBarBox>
                    <div>Last: {{  }}</div>
                    <div>Average: {{  }}</div>
                    <div>Growth from the start: {{  }}</div>
                </leftBarBox>
            </div>
        </div>

        <div class="dataCell">
            <h3 class="sectnHead">All simulations</h3>
            
            <div class="sectnContent">
                <ChartComponent></ChartComponent>
            </div>
        </div>

        <div class="dataCell">
            <h3 class="sectnHead">Last 10 simulations</h3>
            
            <div class="sectnContent">
                aaa
            </div>
        </div>
    </popupControl>
</template>

<style>
</style>