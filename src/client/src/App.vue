<script setup>
  import { ref, computed } from 'vue';
  import { RouterView } from 'vue-router'
</script>

<template>
  <div class="page">
    <div class="header">
      <div class="navigation" id="read" @click="$router.push({ name: 'read-data', params: {} })"><a>Read</a></div>
      <div class="navigation" id="write" @click="$router.push({ name: 'ctrl-panel', params: {} })"><a>Control</a></div>
      <div class="navigation" id="theme" @click=""><img id="theme-icon" src="@/img/light-256.png"></div>
    </div>
    <div class="content">
      <RouterView />
    </div>
  </div>
  
</template>

<style>
.navigation {
  padding: 0.5%;
  padding-left: 1%;
  padding-right: 1%;

  margin-left: 0.2%;
  margin-right: 0.2%;

  border-style: solid;
  border-bottom-style: none;
  border-width: 2px;

  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  border-bottom-left-radius: 0;
  border-bottom-right-radius: 0;

  border-color: #3d3d3d;

  background-color: #efe3da;
}

.page {
  background-color: #d5c4b7;
  height: 100%;
  width: 100%;
  margin: 0;
  padding: 0;
}

.header {
  background-color: #d5c4b7;
  border-color: #3d3d3d;

  border-bottom-width: 2px;
  border-bottom-style: solid;
  
  margin: 0;
  padding: 0;

  display: flex;
}

.content {
  background-color: #efe3da;
  margin: 0%;
  padding: 0%;
}

#read {

}

#control {

}

#theme-icon {
  width: 24px;
  height: 24px;
}
</style>