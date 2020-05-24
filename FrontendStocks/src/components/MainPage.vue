<template>
  <div class="main-page">
    <div>
      <span>Seleccione Securitie: </span>
      <select v-model="selectedSecuritie">
        <option :value="null"></option>
        <option v-for="securitie in securities" :value="securitie.symbol">{{securitie.name}}</option>
      </select>
    </div>
    <div>
      <div style="height:800px;width:800px;" id="securitiesChart">
    </div>
    </div>
  </div>
</template>

<script>

  import echarts from 'echarts'
  import superagent from 'superagent'

  export default {
    data() {
      return {
        selectedSecuritie: null,
        securities: []
      }
    },
    mounted() {
      this.getSecurities()
    },
    methods: {
      getSecurities() {
        superagent.get('http://localhost:5001/securitie/').then(data=> {
          this.securities = data.body
        })
      },
      paintSecuritie(data) {
        const myChart = echarts.init(document.getElementById('securitiesChart'))

        const option = {
            xAxis: {
                type: 'category',
                data: data.labels
            },
            yAxis: {
                type: 'value'
            },
            series: [{
                data: data.dataset,
                type: 'line'
            }]
        }

        myChart.setOption(option)
      }
    },
    watch: {
      selectedSecuritie(newVal) {
        const url = `http://localhost:5001/data/?symbol=${newVal}`
        superagent.get(url).then(data=> {
          const labels = data.body.labels
          const dataset = data.body.dataset
          this.paintSecuritie({labels: labels, dataset: dataset})
        })


      }
    }
  }
</script>

<style scoped>
  .main-page {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
</style>
