<template>
  <div class="tabs" v-model="selectedStock">
    <div
      class="tab-element"
      :class="{'tab-element--selected' : selectedStock == stock.symbol}"
      v-for="stock in stocks" @click="emitValue(stock.symbol)">
      {{stock.name}}
    </div>
  </div>
</template>

<script>

  import superagent from "superagent";

  export default {
    data() {
      return {
        selectedStock: null,
        stocks: []
      }
    },
    methods: {
      getStocks() {
        const url = `http://localhost:5001/`
        superagent.get(url).then(data=> {
          this.stocks = data.body
        })
      },
      emitValue(selectedStock) {
        this.selectedStock = selectedStock
        this.$emit('selectedStock', selectedStock)
      }
    },
    beforeMount(){
        this.getStocks()
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
