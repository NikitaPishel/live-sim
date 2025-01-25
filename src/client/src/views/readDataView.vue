<!-- Page where you can read info about simulation  -->

<script>

</script>

<template>
    <div class="popupPanel">
        <div class="popupCell">
            <h3 class="sectnHead">Genomes </h3>

            <div class="sectnContent">
                <button class="menuButton">Open menu</button>
            </div>
        </div>

        <div class="popupCell">
            <h3 class="sectnHead">Amount of passed agents</h3>
            
            <div class="sectnContent">
                <button class="menuButton">Open menu</button>
                <div class="miniData">Hello World</div>
            </div>
        </div>

        <div class="popupCell">
            <h3 class="sectnHead">Survivability percentage</h3>
            <div class="sectnContent">
                <button class="menuButton">Open menu</button>
                <div class="miniData">
                    <p>Hello World</p>
                    <p>Hello World</p>
                    <p>Hello World</p>
                </div>
            </div>
        </div>
    </div>
</template>

<style>

.menuButton {
    border-style: solid;
    border-radius: 0%;
    border-width: 2px;
    border-color: #3d3d3d;

    width: 72px;
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

.popupCell {
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