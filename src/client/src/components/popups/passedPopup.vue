<!-- Popup menu with genomes -->

<script setup>
import { computed } from 'vue';
import { usePopupStore } from '@/stores/popupStore.js';
import popupControl from '@/components/popups/popupControl.vue';
import leftBarBox from '@/components/dataBoxes/leftBarBox.vue'
import ChartComponent from '@/components/charts/ChartComponent.vue';

const popupStore = usePopupStore()
const passedNum = computed (() => popupStore.popupsDisplay.passedNum)
</script>

<template>
<popupControl v-if="passedNum" :displayState="'passedNum'">
    <div class="dataCell">
        <h3 class="panelHead">Amount of passed agents</h3>
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