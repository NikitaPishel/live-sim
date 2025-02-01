<!-- Page where you can control server from client  -->

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
    <div class="controlPanel">
        <div class="dataCell">
            <h3 class="panelHead">Control Panel</h3>
        </div>

        <div class="dataCell">
            <h3 class="sectnHead">Control</h3>

            <div class="sectnContent">
                <button class="ctrlButton">Pause</button>
                <button class="ctrlButton">Shutdown</button>
            </div>
        </div>

        <div class="dataCell">
            <leftBarBox>
                <a>Current iteration: </a>
                <a>Last Iteration: </a>
            </leftBarBox>

            <leftBarBox>
                <a>Time since start of the session: </a>
                <a>Average time per iteration: </a>
            </leftBarBox>

            <leftBarBox>
                <a>Last Iteration Survivability: </a>
                <a>Survivability Growth: </a>
            </leftBarBox>
        </div>
    </div>
</template>

<style scoped>
.ctrlButton {
    border-style: none;
    border-radius: 4px;
    border-width: 1px;
    border-color: #727272;
    background-color: #efe3da;

    width: 96px;
    margin: 1%;
    padding: 1.5%;
}

.controlPanel {
    margin: 1%;
    padding: 0%;
    padding-top: 6%;
    padding-bottom: 8%;
}
</style>