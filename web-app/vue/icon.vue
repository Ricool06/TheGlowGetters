<template>
<div class="icon">
  <div class="icon__fragment1"></div>
  <div class="icon__fragment2"></div>
  <div class="icon__fragment3"></div>
  <div class="icon__fragment4"></div>
  <div class="icon__fragment5"></div>
  <div class="icon__fragment6"></div>
  <div class="icon__fragment7"></div>
  <div class="icon__fragment8"></div>
  <div class="icon__fragment9"></div>
  <div class="icon__fragment10"></div>
</div>
</template>

<script>
module.exports = {
}
</script>

<style>
/*
 * ## Icon elements
 */
.icon {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  grid-template-rows: repeat(6, 1fr);
  grid-column-gap: 1px;
  grid-row-gap: 1px;
  padding: 1px;
  background-color: white;
  width: 14px; /* 10px */
  height: 17px; /* 11px */
}
.icon > div {background-color: var(--blue);}
.icon__fragment1 {grid-area: 3 / 3 / 4 / 5;}
.icon__fragment2 {grid-area: 3 / 4 / 6 / 5;}
.icon__fragment3 {grid-area: 5 / 1 / 6 / 5;}
.icon__fragment4 {grid-area: 1 / 1 / 6 / 2;}
.icon__fragment5 {grid-area: 1 / 1 / 2 / 6;}
.icon__fragment6 {grid-area: 4 / 2 / 5 / 4;}
.icon__fragment7 {grid-area: 2 / 2 / 5 / 3;}
.icon__fragment8 {grid-area: 2 / 2 / 3 / 6;}
.icon__fragment9 {grid-area: 2 / 5 / 7 / 6;}
.icon__fragment10 {grid-area: 6 / 1 / 7 / 6;}
</style>
