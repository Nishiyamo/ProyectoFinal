<template>
  <div class="main">
    <Tabs @selectedStock="setSelectedStock"></Tabs>
    <ChartController v-if="selectedStock" :selectedStock="selectedStock"></ChartController>
  </div>
</template>

<script>
  import Tabs from './Tabs'
  import ChartController from './ChartController'

  export default {
    components: {Tabs, ChartController},
    data() {
      return {
        selectedStock: null
      }
    },
    methods: {
      setSelectedStock(value) {
        this.selectedStock = value
      }
    }
  }
</script>

<style scoped>

  .main {
    display:flex;
    flex-direction: column;
    align-items: center;
  }

</style>
