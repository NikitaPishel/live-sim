<!-- Page where you can read info about simulation  -->

<script>

</script>

<template>
    <div class="popupPanel">
        <div class="dataCell">
            <h3 class="panelHead">Read Panel</h3>
        </div>

        <div class="dataCell">
            <h3 class="sectnHead">Genomes </h3>

            <div class="sectnContent">
                <button class="menuButton">Open menu</button>
            </div>
        </div>

        <div class="dataCell">
            <h3 class="sectnHead">Amount of passed agents</h3>
            
            <div class="sectnContent">
                <button class="menuButton">Open menu</button>
                <div class="miniData">
                    <div>
                        <a>Last: </a>
                        <a></a>
                    </div>
                    
                    <div>
                        <a>Average: </a>
                        <a></a>
                    </div>
                    
                    <div>
                        <a>Growth from the start: </a>
                        <a></a>
                    </div>
                </div>
            </div>
        </div>

        <div class="dataCell">
            <h3 class="sectnHead">Survivability percentage</h3>
            <div class="sectnContent">
                <button class="menuButton">Open menu</button>
                <div class="miniData">
                    <div>
                        <a>Last: </a>
                        <a></a>
                    </div>
                    
                    <div>
                        <a>Average: </a>
                        <a></a>
                    </div>
                    
                    <div>
                        <a>Growth from the start: </a>
                        <a></a>
                    </div>
                </div>
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

.menuButton {
    border-style: solid;
    border-radius: 24px;
    border-width: 1px;
    border-color: #3d3d3d;

    width: 72px;
    height: 5%;
    margin: 5px;
    padding: 1%;
}
</style>