<template>
  <div class="tabs">
    <div
      class="tab-element"
      :class="{'tab-element--selected' : selectedStock == stock.symbol}"
      v-for="stock in stocks" @click="emitValue(stock.symbol)">
      {{stock.name}}
    </div>
  </div>
</template>

<script>

  export default {
    data() {
      return {
        selectedStock: null,
        stocks: [{
          name: 'Indice bursatil de España',
          symbol: 'IBEX'
        }, {
          name: 'Indice bursatil de Estados Unidos',
          symbol: 'IXIC'
        }, {
          name: 'Indice bursatil de Londres',
          symbol: 'FTSE'
        }]
      }
    },
    methods: {
      emitValue(selectedStock) {
        this.selectedStock = selectedStock
        this.$emit('selectedStock', selectedStock)
      }
    }
  }
</script>

<style scoped>
  .tabs {
    display: flex;
    align-items: center;
    flex-direction: row;
    margin-bottom: 3rem;
  }

  .tab-element {
    height: 50px;
    width: 400px;
    text-align: center;
    border: 1px solid black;
  }

  .tab-element:hover {
    cursor: pointer;
    background: lightblue;
  }

  .tab-element--selected {
    background: dodgerblue;
  }
</style>
