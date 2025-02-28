<!-- Sign in page  -->

<script>

</script>

<template>
    <div class="centerBox">
        <div class="signContainer">
            <div class="dataCell">
                <div id="logoDiv"><img id="logoIcon" src="../img/logo.png"></div>
                <h3 class="panelHead">Sign in</h3>
            </div>

            <div class="dataCell">
                
                <div class="signBox">
                    <h3 class="signHead">Username</h3>
                    
                    <div class="field">
                        <input class="textField" type="text"></input>    
                    </div>
                
                </div>
                
                <div class="signBox">
                    <h3 class="signHead">Password</h3>
                    
                    <div class="field">
                        <input class="textField" type="password"></input>
                    </div>                    
                </div>

            </div>

            <div class="dataCell">
                <button id="submitButton">Submit</button>
            </div>
        </div>
    </div>
</template>

<style scoped lang="scss">
#logoDiv {
    display: flex;
    justify-content: center;
    align-items: center;
}

#logoIcon {
    width: 128px;
    height: 128px;
}

#submitButton {
    border-style: none;
    border-radius: 4px;
    border-width: 1px;
    border-color: #727272;

    background-color: rgba(239, 227, 218, 1);
    color: rgba(61, 61, 61, 1);

    cursor: pointer;

    width: 128px;
    margin: 2%;
    padding: 1%;
    font-size: 24px;

    &:hover {
        background-color: rgba(243, 231, 222, 1);
    }
}

.centerBox {
    display: flex;
    justify-content: center;
    align-items: center;
}

.signContainer {
    margin: 12%;
    width: 40%;
}

.signBox {
    margin: 2%;
}

.textField {
    margin: 0%;
    border-style: none;
    border-bottom-style: none;
    border-color: #3d3d3d;
    border-width: 1px;
    border-radius: 24px;
    
    background-color: rgba(239, 227, 218, 1);;
    color: rgba(61, 61, 61, 1);
    
    margin: 1%;
    padding: 2%;
    padding-left: 4%;
    padding-right: 4%;

    font-size: 14px;
    overflow: hidden;

    &:hover {
        background-color: rgba(243, 231, 222, 1);
    }
}

.signHead {
    font-size: 24px;
    margin: 2%;
}

/* dark */
.dark {
    #submitButton {
        border-style: none;
        border-radius: 4px;
        border-width: 1px;
        border-color: #727272;

        background-color: rgba(10, 10, 16, 1);;
        color: rgba(254, 250, 243, 1);

        cursor: pointer;
        
        width: 128px;
        margin: 2%;
        padding: 1%;
        font-size: 24px;

        &:hover {
            background-color: rgba(14, 14, 20, 1);
        }
    }

    .textField {
        margin: 0%;
        border-style: none;
        border-bottom-style: none;
        border-color: #3d3d3d;
        border-width: 1px;
        border-radius: 24px;
        
        background-color: rgba(10, 10, 16, 1);
        color: rgba(254, 250, 243, 1);;
        
        margin: 1%;
        padding: 2%;
        padding-left: 4%;
        padding-right: 4%;
        
        font-size: 14px;
        overflow: hidden;
        
        &:hover {
            background-color: rgba(14, 14, 20, 1);
        }
    }
}
</style>