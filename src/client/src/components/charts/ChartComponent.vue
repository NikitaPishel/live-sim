<script>
import { onMounted } from 'vue';
import Chart from 'chart.js/auto';

export default {
  setup() {
    onMounted(() => {
      const chartPath = document.getElementById('chart');

      const data = {
        labels: ["1", "2", "3", "4"],
        datasets: [{
          label: 'My First Dataset',
          data: [57, 63, 80, 69],
          fill: false,
          borderColor: 'rgb(255, 180, 98)',
          tension: 0,
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