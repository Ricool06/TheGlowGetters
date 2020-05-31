<template>
<div class="graph">
  <img class="graph__img" :src="url">
</div>
</template>

<script>
module.exports = {
  props: {
    url: String
  },
  methods: {
  }
}
</script>

<style>
/*
 * ## Graph elements
 */
.graph {
    border-bottom: 1px solid var(--border-color);
}
.graph__img {
    width: calc(100% - 10px);
    margin: 4px;
    display: block;
    border: 1px solid var(--border-color);
}
</style>
