<!-- Page where you can read info about simulation  -->

<script>
import leftBarBox from '@/components/dataBoxes/leftBarBox.vue'
import { ref } from 'vue'

export default {
    components: {
        leftBarBox
    }
}

</script>

<template>
    <div class="popupPanel">
        <div class="dataCell">
            <h3 class="panelHead">Read Panel</h3>
        </div>
        <div class="dataCell">
            <h3 class="sectnHead">Genomes </h3>
            <div class="sectnContent">
                <button class="popupButton">Open menu</button>
            </div>
        </div>

        <div class="dataCell">
            
            <h3 class="sectnHead">Amount of passed agents</h3>
            <div class="sectnContent">
                <button class="popupButton">Open menu</button>
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
                <button class="popupButton">Open menu</button>
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
</template>

<style scoped>

.popupButton {
    border-style: none;
    border-radius: 24px;
    border-width: 1px;
    border-color: #3d3d3d;

    background-color: #efe3da;

    width: 72px;
    height: 5%;
    margin: 5px;
    padding: 1%;
}
</style>