<!-- Page where you can control server from client  -->

<script>

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
            <div class="miniData">
                <div>
                    <a>Current iteration: </a>
                    <a></a>
                </div>
                <div>
                    <a>Last Iteration: </a>
                    <a></a>
                </div>
            </div>

            <div class="miniData">
                <div>
                    <a>Time since start of the session: </a>
                    <a></a>
                </div>
                <div>
                    <a>Average time per iteration: </a>
                    <a></a>
                </div>
            </div>

            <div class="miniData">
                <div>
                    <a>Last Iteration Survivability: </a>
                    <a></a>
                </div>
                <div>
                    <a>Survivability Growth: </a>
                    <a></a>
                </div>
            </div>
        </div>
    </div>
</template>

<style>
.ctrlButton {
    border-style: solid;
    border-radius: 24px;
    border-width: 1px;
    border-color: #3d3d3d;

    width: 96px;
    height: 5%;
    margin: 5px;
    padding: 1%;
}

.controlPanel {
    margin: 1%;
    padding: 0%;
    padding-top: 6%;
    padding-bottom: 8%;
}
</style>