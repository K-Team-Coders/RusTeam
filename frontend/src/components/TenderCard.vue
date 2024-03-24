<template>
  <div>
    <div class="pt-3 w-full">
      <div
        class="border-neutral-200 border-[0.5px] px-4 py-3 rounded-md flex justify-between w-full duration-300"
      >
        <div class="w-7/12 flex flex-col gap-2 duration-300">
          <div>
            <p
              @click="isModalOpen = true"
              class="text-activeText font-medium text-lg tracking-widest duration-300 hover:underline hover:duration-150 cursor-pointer"
            >
              Закупка ТМЦ (пластины)
            </p>
            <p class="text-activeText duration-300 font-light tracking-wide">
              ООО "Протехстрой"
            </p>
          </div>
          <ModalWindow v-if="isModalOpen" @close="isModalOpen = false" />
          <p
            class="text-neutral-500 duration-300 pt-2 font-normal tracking-wide"
          >
            Коммерческие, № 12736748 от 23.03.2024
          </p>
        </div>
        <div class="w-2/12 text-end">
          <p class="text-activeText text-xl font-bold">756 000,00</p>
          <p class="text-activeText tracking-wide pt-1">Перейти на ЭТП</p>
        </div>
        <div class="w-3/12 text-end">
          <p class="text-activeText font-semibold">
            Порядок заявок до 28.03.2024
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ModalWindow from "./ModalWindow.vue";
export default {
  components: {
    ModalWindow,
  },
  data() {
    return {
      isModalOpen: false,
    };
  },
  emits: ["close"],
};
</script>
