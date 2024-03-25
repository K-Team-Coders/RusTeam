<template>
  <div class="duration-500">
    <input
      type="checkbox"
      id="darkmode-toggle"
      v-model="darkMode"
      @change="toggleDarkMode"
    />
    <label for="darkmode-toggle"> </label>
  </div>
</template>
<script>
import { mapState, mapActions } from "vuex";

export default {
  computed: {
    ...mapState(["darkMode"]),
  },
  methods: {
    ...mapActions(["toggleDarkMode"]),
  },
};
</script>
<style scoped>
label {
  width: 100px;
  height: 20px;
  position: relative;
  display: block;
  background: #ebebeb;
  border-radius: 200px;
  box-shadow: inset 0px 5px 15px rgba(0, 0, 0, 0.4),
    inset 0px -5px 15px rgba(255, 255, 255, 0.4);
  cursor: pointer;
  transition: 0.3s;
  &:after {
    content: "";
    width: 46px;
    height: 15px;
    position: absolute;
    top: 2.5px;
    left: 4px;
    background: linear-gradient(180deg, #ffcc898e, #d8860b8b);
    border-radius: 180px;
    box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.2);
    transition: 0.3s;
  }
  svg {
    position: absolute;
    width: 14px;
    top: 2.8px;
    z-index: 100;
    &.sun {
      left: 19px;
      fill: #fff;
      transition: 0.3s;
    }
    &.moon {
      left: 68px;
      fill: #7e7e7e;
      transition: 0.3s;
    }
  }
}

input {
  width: 0;
  height: 0;
  visibility: hidden;
  &:checked + label {
    background: #242424;
    &:after {
      left: 96px;
      transform: translateX(-100%);
      background: linear-gradient(180deg, #777, #3a3a3a);
    }
    svg {
      &.sun {
        fill: #7e7e7e;
      }
      &.moon {
        fill: #fff;
      }
    }
    + .background {
      background: #242424;
    }
  }
  &:active:after {
    width: 250px;
  }
}

.background {
  width: 100vw;
  height: 100vh;
  background: #fff;
  z-index: -1;
  position: absolute;
  transition: 0.3s;
}
</style>
