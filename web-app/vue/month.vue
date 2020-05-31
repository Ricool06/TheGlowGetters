<template>
<div class="month">
    <div class="month__name">{{name}}</div>
    <div class="month__days">
      <template v-for="day, idx in days">
        <div :class="[
          'month__day',
          'month__day--'+day,
          available_days.includes(idx+1) ? 'month__day--available' : '',
          idx+1 == active_day ? 'month__day--active' : '']"
          @mousedown="open_day(idx+1)"></div>
      </template>
    </div>
</div>
</template>

<script>
module.exports = {
  props: {
    name: String,
    year: Number,
    available_days: Array,
    active_day: Number
  },
  methods: {
    open_day: function (day) {
      idx = this.available_days.indexOf(day)
      if (idx == -1)
        return
      this.$root.$emit('open_day', idx, this.name);
    }
  },
  computed: {
    days: function () {
      if (
        this.name == 'September' ||
        this.name == 'April' ||
        this.name == 'June' ||
        this.name == 'November') {
        return 30;
      } else if (this.name == 'February') {
        return 28;
      } else {
        return 31;
      }
    }
  }
}
</script>

<style>
/*
 * ## Month elements
 */
.month {
  display: flex;
  flex-direction: column;
  padding: 16px;
}
.month__name {
  font-family: 'Roboto', sans-serif;
  font-weight: bold;
  padding-bottom: 8px;
}
.month__days {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  grid-template-rows: repeat(5, 1fr);
  grid-column-gap: 8px;
  grid-row-gap: 8px;
}
.month__day {
  border: 1px solid var(--border-color);
  height: 14px;
}
.month__day--available {
  background-color: var(--shadow);
  cursor: pointer;
}
.month__day--active {
  background-color: var(--cyan);
}
</style>
