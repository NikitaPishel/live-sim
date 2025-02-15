<script setup>
  import { ref, computed } from 'vue';
  import { RouterView } from 'vue-router';

  const themeName = ref('dark')
  const themeIcon = ref("/src/img/light-256.png")
  const signIcon = ref("/src/img/sign-light-256.png")
  
  
  const switchTeme = () => {
    console.log('Switching theme')
    
    if (themeName.value === 'dark') {
      themeName.value = 'light';
      themeIcon.value = '/src/img/dark-256.png';
      signIcon.value = "/src/img/sign-dark-256.png"
    }
    
    else {
      themeName.value = 'dark';
      themeIcon.value = '/src/img/light-256.png';
      signIcon.value = "/src/img/sign-light-256.png"
    };
  };
</script>

<template>
  <main :class="themeName">
    <div class="page">
      <div class="header">
        <div class="navigation" id="read" @click="$router.push({ name: 'read-data', params: {} })"><a>Read</a></div>
        <div class="navigation" id="write" @click="$router.push({ name: 'ctrl-panel', params: {} })"><a>Control</a></div>
        <div class="navigation" id="theme" @click="$router.push({ name: 'sign-in', params: {} })">Sign</div>
        <div class="navigation" id="theme" @click="switchTeme"><img id="theme-icon" :src="themeIcon"></div>
      </div>
      <div class="pageContainer">
        <div class="content">
          <RouterView />
        </div>
      </div>
    </div>
  </main>
</template>

<style lang="scss">
  
  #theme-icon {
    width: 18px;
    height: 18px;
  }

</style>