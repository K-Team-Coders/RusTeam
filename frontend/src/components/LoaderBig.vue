<template>
  <div>
    <AnimatedText />
  </div>
</template>
<script>
import AnimatedText from "./AnimatedText.vue";

export default {
  computed: {
    isDarkMode() {
      return this.$store.state.darkMode;
    },
  },
  components: { AnimatedText },
};
</script>
