<script setup>
  import { ref, computed } from 'vue';
  import { RouterView } from 'vue-router';

  const themeName = ref('dark')
  const themeIcon = ref("/src/img/theme-light.png")
  const profileIcon = ref("/src/img/profile-light.png")
  
  
  const switchTeme = () => {
    console.log('Switching theme')
    
    if (themeName.value === 'dark') {
      themeName.value = 'light';
      themeIcon.value = '/src/img/theme-dark.png';
      profileIcon.value = "/src/img/profile-dark.png"
    }
    
    else {
      themeName.value = 'dark';
      themeIcon.value = '/src/img/theme-light.png';
      profileIcon.value = "/src/img/profile-light.png"
    };
  };

</script>

<template>
  <main :class="themeName">
    <div class="page">
      <div class="header">
        <div class="navigation" id="read" @click="$router.push({ name: 'read-data', params: {} })"><a>Read</a></div>
        <div class="navigation" id="write" @click="$router.push({ name: 'ctrl-panel', params: {} })"><a>Control</a></div>
        <div class="navigation" id="theme" @click="$router.push({ name: 'sign-in', params: {} })"><img id="profile-icon" :src="profileIcon"></div>
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

  #profile-icon {
    width: 18px;
    height: 18px;
  }
</style>