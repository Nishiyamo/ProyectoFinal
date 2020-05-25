<template>
  <div class="chart-controller">
    <div>
      <span>Seleccione Valor de bolsa: </span>
      <select v-model="selectedSecuritie">
        <option :value="null"></option>
        <option v-for="securitie in securities" :value="securitie.symbol">{{securitie.name}}</option>
      </select>
    </div>
    <div>
      <div style="height:700px;width:1600px;" id="securitiesChart">
    </div>
    </div>
  </div>
</template>

<script>

  import echarts from 'echarts'
  import superagent from 'superagent'

  export default {
    props: {
      selectedStock: String
    },
    data() {
      return {
        selectedSecuritie: null,
        securities: []
      }
    },
    methods: {
      getSecurities(newVal) {
        const url = `http://localhost:5001/securitie/?stock=${newVal}`
        superagent.get(url).then(data=> {
          this.securities = data.body
        })
      },
      paintSecuritie(data, newVal) {
        const myChart = echarts.init(document.getElementById('securitiesChart'))

        const option = {
            title:{
              text: newVal
            },
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                  type: 'cross'
                }
            },
            legend:{
            },
            grid: {
                left: '3%',
                right: '4%',
                bottom: '3%',
                containLabel: true
            },
            xAxis: {
                type: 'category',
                boundaryGap: false,
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
          this.paintSecuritie({labels: labels, dataset: dataset},newVal)
        })
      },
      selectedStock(newVal) {
        this.getSecurities(newVal)
      }
    }
  }
</script>

<style scoped>
  .chart-controller {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
</style>
