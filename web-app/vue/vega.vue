<template>
<div :class="['vega', region]"></div>
</template>

<script>
var yourVlSpec =
module.exports = {
  props: {
    region: String
  },
  watch: {
    region: {
      immediate: true, 
      handler () {
        if (this.$el)
          this.$el.innerHTML = ""; 
        fetch(`/json/${this.region}.json`)
        .then(response => response.json())
        .then(json => {
          this.vega = vegaEmbed(`.${this.region}`, json, {
            actions: {
              export: true,
              source: false,
              compiled: false,
              editor: false
            },
            downloadFileName: "chart"
          });
        });
      }
    }
  }
}
</script>

<style>
.vega {
  width: 90%;
}
</style>
