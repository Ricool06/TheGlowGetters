<template>
<div class="item" @mousedown="open_item">
    <div class="item__name">{{name}}</div>
    <div class="item__latitue">Latitude</div>
    <div class="item__latitude_min">{{latitude[0]}}</div>
    <div class="item__latitude_max">{{latitude[1]}}</div>
    <div class="item__logitude">Longitude</div>
    <div class="item__logitude_min">{{logitude[0]}}</div>
    <div class="item__logitude_max">{{logitude[0]}}</div>
</div>
</template>

<script>
module.exports = {
  props: {
    name: String,
    latitude: Array,
    logitude: Array,
    idx: Number
  },
  methods: {
    open_item: function (event) {
      this.$root.$emit('open_item', this.idx);
    }
  }
}
</script>

<style>
/*
 * ## Item elements
 */
.item {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-template-rows: repeat(3, 1fr);
    grid-column-gap: 0px;
    grid-row-gap: 0px;
    padding: 16px;
    border-bottom: 1px solid var(--border-color);
    cursor: pointer;
}
.item__name {
    grid-area: 1 / 1 / 2 / 4;
    font-family: 'Roboto', sans-serif;
    font-weight: bold;
}
.item__latitue { grid-area: 2 / 1 / 3 / 2; }
.item__latitude_min { grid-area: 2 / 2 / 3 / 3; }
.item__latitude_max { grid-area: 2 / 3 / 3 / 4; }
.item__logitude { grid-area: 3 / 1 / 4 / 2; }
.item__logitude_min { grid-area: 3 / 2 / 4 / 3; }
.item__logitude_max { grid-area: 3 / 3 / 4 / 4; }
</style>
