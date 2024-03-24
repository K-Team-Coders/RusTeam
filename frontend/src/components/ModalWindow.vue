<template>
  <div
    class="fixed pt-3 inset-0 z-50 focus:outline-none duration-500 bg-neutral-800/80"
    @click.self="close"
    tabindex="-1"
    @keydown.esc="close"
  >
    <div
      class="bg-neutral-100 rounded-lg max-w-3xl mx-auto xl:my-2 flex flex-col shadow-4xl relative"
    >
      <div class="">
        <ModalWindowButtonClose @click="close" class="absolute right-0" />
      </div>
      <div class="pt-10 flex justify-center relative">
        <p class="font-semibold text-sm absolute left-4 top-3">ID: 12378172</p>
        <div class="w-9/12 items-center flex flex-col">
          <p class="pb-3 font-bold text-xl">tender_name</p>
        </div>
      </div>
      <div class="px-8 pb-4 w-full">
        <p class="pb-2">
          <span class="font-bold"> data_created: </span> Lorem, ipsum dolor sit
          amet consectetur adipisicing elit. Incidunt veniam voluptatibus
          mollitia a amet explicabo accusantium odio voluptates. Asperiores
          animi, illo dolores atque quisquam voluptas fugit nostrum explicabo
          quam laboriosam.
        </p>
        <p class="pb-2">
          <span class="font-bold">data_execution:</span> Lorem ipsum dolor sit
          amet consectetur adipisicing elit. Aliquam veniam dolores cupiditate
          esse autem nostrum ut dicta accusantium architecto sequi labore,
          reiciendis expedita! Cupiditate, asperiores. Soluta laudantium
          accusantium totam modi.
        </p>
        <p class="pb-2">
          <span class="font-bold">documents:</span> Lorem, ipsum dolor sit amet
          consectetur adipisicing elit. Sapiente, omnis labore nemo praesentium
          amet aliquam ut velit esse, temporibus, molestiae facilis ex. Enim
          atque odio rem corporis et ex impedit.
        </p>
        <p class="pb-2">
          <span class="font-bold">organization:</span> Lorem ipsum dolor sit
          amet consectetur adipisicing elit. Nemo delectus voluptates,
          voluptatem laudantium aperiam facere aut laborum illo numquam
          quibusdam, architecto ducimus asperiores. Iusto natus, alias ratione
          deserunt asperiores quasi.
        </p>
      </div>
    </div>
  </div>
</template>
<script>
import ModalWindowButtonClose from "./ModalWindowButtonClose.vue";

export default {
  components: {
    ModalWindowButtonClose,
  },
  methods: {
    close() {
      this.$emit("close");
    },
  },
  mounted() {
    this.$el.focus();
  },
  emits: ["close"],
};
</script>
