<script>
import { onMounted } from 'vue';
import Chart from 'chart.js/auto';

export default {
  setup() {
    onMounted(() => {
      const chartPath = document.getElementById('chart');

      const data = {
        labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        showLines: true,
        datasets: [{
          label: 'My First Dataset',
          data: [25, 47, 65, 73, 80, 76, 83, 85, 76, 88, 91, 93],
          fill: false,
          borderColor: 'rgb(255, 180, 98)',
          tension: 0.5,
          width: '256px',
          height: '144px',
        }]
      };

      const chartConfig = {
        type: 'line',
        data: data,
      };

      new Chart(chartPath, chartConfig);
    });
  }
};
</script>

<template>
    <div>
        <canvas id="chart"></canvas>
    </div>
</template>

<style>
</style>