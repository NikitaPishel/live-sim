<!-- Page where you can read info about simulation  -->

<script setup>
import genomePopup from '@/components/popups/genomePopup.vue';
import passedPopup from '@/components/popups/passedPopup.vue';
import survivPopup from '@/components/popups/survivPopup.vue';

import leftBarBox from '@/components/dataBoxes/leftBarBox.vue'
import popupControl from '@/components/popups/popupControl.vue';
import { usePopupStore } from '@/stores/popupStore.js';

import { ref, computed } from 'vue'

const popupStore = usePopupStore()

const switchPopup = popupStore.switchPopup

const genome = computed (() => popupStore.popupsDisplay.genome)
</script>

<template>
    <div class="popupPanel">
        <div class="dataCell">
            <h3 class="panelHead">Read Panel</h3>
        </div>
        <div class="dataCell">
            <h3 class="sectnHead">Genomes </h3>
            <div class="sectnContent">
                <button class="popupButton" @click="() => switchPopup('genome')">Open menu</button>
            </div>
        </div>

        <div class="dataCell">
            
            <h3 class="sectnHead">Amount of passed agents</h3>
            <div class="sectnContent">
                <button 
                class="popupButton" @click="() => switchPopup('passedNum')">Open menu</button>
                <leftBarBox>
                    <div>Last: {{  }}</div>
                    <div>Average: {{  }}</div>
                    <div>Growth from the start: {{  }}</div>
                </leftBarBox>
            </div>
        </div>

        <div class="dataCell">
            <h3 class="sectnHead">Survivability percentage</h3>
            <div class="sectnContent">
                <button class="popupButton" @click="() => switchPopup('surviv')">Open menu</button>
                <leftBarBox>
                    <div>Last: {{  }}</div>
                    <div>Average: {{  }}</div>
                    <div>Growth from the start: {{  }}</div>
                </leftBarBox>
            </div>
        </div>

        <div class="dataCell">
            <leftBarBox>
                <div>Current iteration: {{  }}</div>
                <div>Last Iteration: {{  }}</div>
            </leftBarBox>
            <leftBarBox>
                <div>Time since start of the session: </div>
                <div>Average time per iteration: </div>
            </leftBarBox>

            <leftBarBox>
                <div>Last Iteration Survivability: </div>
                <div>Survivability Growth: </div>
            </leftBarBox>
        </div>
    </div>

    <genomePopup />
    <passedPopup />
    <survivPopup />
</template>

<style scoped>

</style>