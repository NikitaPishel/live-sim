<!-- Page where you can control server from client  -->

<script>

</script>

<template>
    <div class="popupPanel">
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

.fillScreen {
    overflow: hidden;
}

.ctrlButton {
    border-style: solid;
    border-radius: 0%;
    border-width: 2px;
    border-color: #3d3d3d;

    width: 96px;
    height: 5%;
    margin: 5px;
    padding: 1%;
}

.miniData {
    border-left-style: solid;
    border-color: #3d3d3d;
    border-width: 2px;

    margin: 0.5%;
    padding: 0.5%;
}

.dataCell {
    border-style: solid;
    border-width: 2px;
    border-color: #3d3d3d;

    color: #3d3d3d;

    margin: 1%;
    padding: 1%;
}

.sectnContent {
    display: flex;
}

.sectnHead {
    font-size: 16px;
}

.popupPanel {
    padding: 12px;
    background-color: #efe3da;
}
</style>