<template>
  <div>
    <ModalWindow v-if="isModalOpen" @close="isModalOpen = false" :tender_info="tender_info"/>
    <div class="pt-3 w-full">
      <div
        @click="isModalOpen = true"
        class="border-neutral-200 cursor-pointer border-[0.5px] pr-4  rounded-md flex justify-between w-full duration-300"
      >
        <div class=" w-[3%] bg-red-600 rounded-l-md mr-2"></div>
        <div class="w-6/12 flex flex-col gap-2 duration-300 py-3">
          <div>
            <p
              class="text-activeText font-medium text-lg tracking-widest duration-300 hover:underline hover:duration-150"
            >
              {{ tender_info.tender_name }}
            </p>
            <p class="text-activeText duration-300 font-light tracking-wide">
              {{ tender_info.organization }}
            </p>
          </div>
          <p
            class="text-neutral-500 duration-300 pt-2 font-normal tracking-wide"
          >
            ID{{ tender_info.tender_id.slice(2) }} от
            {{ tender_info.data_created.slice(14) }}
          </p>
        </div>
        <div class="w-2/12 text-end py-3">
          <a
            :href="`${tender_info.url}`" target="_blank"
            class="text-activeText tracking-wide pt-1"
            >Перейти на страницу тендера</a
          >
        </div>
        <div class="w-3/12 text-end py-3">
          <p class="text-activeText font-semibold">
            Прием заявок до {{ tender_info.data_execution.slice(16) }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ModalWindow from "./ModalWindow.vue";
export default {
  props: {
    tender_info: Object,
    color: String,
  },

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
