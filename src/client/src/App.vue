<script setup>
  import { ref, computed } from 'vue';
  import { RouterView } from 'vue-router';
</script>

<template>
  <main>
    <div class="page">
      <div class="header">
        <div class="navigation" id="read" @click="$router.push({ name: 'read-data', params: {} })"><a>Read</a></div>
        <div class="navigation" id="write" @click="$router.push({ name: 'ctrl-panel', params: {} })"><a>Control</a></div>
        <div class="navigation" id="theme" @click=""><img id="theme-icon" src="@/img/light-256.png"></div>
      </div>
      <div class="pageContainer">
        <div class="content">
          <RouterView />
        </div>
      </div>
    </div>
  </main>
</template>

<style>
  
  #theme-icon {
    width: 18px;
    height: 18px;
  }

</style>