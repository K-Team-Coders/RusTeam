<template>
  <div
    class="fixed pt-3 inset-0 z-50 focus:outline-none duration-500 bg-neutral-800/80"
    @click.self="close"
    tabindex="-1"
    @keydown.esc="close"
  >
    <div
      class="bg-neutral-100 rounded-lg max-w-[70vw] max-h-[85vh] mx-auto xl:my-2 flex flex-col shadow-4xl relative"
    >
      <div class="z-50">
        <ModalWindowButtonClose @click="close" class="absolute right-0" />
      </div>
      <div class="pt-10 flex justify-center relative">
        <p class="font-semibold text-sm absolute left-4 top-3">
          ID:{{ tender_info.tender_id.slice(2) }}
        </p>
        <div class="w-9/12 items-center flex flex-col">
          <p class="pb-3 font-bold text-xl">{{ tender_info.tender_name }}</p>
        </div>
      </div>
      <div class="px-8 pb-4 w-full">
        <p class="pb-2">
          <span class="font-bold"> Дата создания: </span>
          {{ tender_info.data_created.slice(14) }}
        </p>
        <p class="pb-2">
          <span class="font-bold">Прием заявок до:</span>
          {{ tender_info.data_execution.slice(16) }}
        </p>
        <p class="pb-2 font-bold">Документы</p>
        <ul>
          <li v-for="doc in tender_info.documents" :key="doc">
            <a
              :href="`${doc.url}`"
              target="_blank"
              class="text-activeText tracking-wide pt-1"
            >
              {{ doc.name }}
            </a>
          </li>
        </ul>
        <p class="pb-2">
          <span class="font-bold">Организация:</span>
          {{ tender_info.organization }}
        </p>

        <span class="font-bold"> Товары: </span>
        <div class="pt-2.5">
          <div
            class="overflow-y-scroll rounded-xl shadow-md h-[45vh] custom-scrollbar"
          >
            <table
              class="w-full text-xs text-normal-500 table-auto 2xl:table-fixed text-center"
            >
              <thead
                class="text-xs text-neutral-700 uppercase bg-neutral-300 font-bold"
              >
                <tr class="">
                  <th
                    scope="col"
                    class="px-1 py-3 w-4 cursor-pointer hover:text-red-600 duration-300"
                  >
                    ID
                  </th>
                  <th
                    scope="col"
                    class="px-1 py-3 cursor-pointer hover:text-red-600 duration-300"
                  >
                    Название
                  </th>
                  <th
                    scope="col"
                    class="px-6 py-3 cursor-pointer hover:text-red-600 duration-300"
                  >
                    Количество
                  </th>
                  <th
                    scope="col"
                    class="px-6 py-3 cursor-pointer hover:text-red-600 duration-300"
                  >
                    Единица измерения
                  </th>
                </tr>
              </thead>
              <tbody class="bg-neutral-200">
                <tr
                  v-for="(good, index) in tender_info.goods"
                  class="border-t-2 border-neutral-400"
                  :key="index"
                >
                  <td class="px-6 py-4">
                    {{ index + 1 }}
                  </td>
                  <td
                    :href="`${good.url}`"
                    target="_blank"
                    class="px-6 py-4 font-medium text-left"
                  >
                    {{ good.name }}
                  </td>
                  <td class="px-6 py-4">
                    {{ good.count }}
                  </td>
                  <td class="px-6 py-4">
                    {{ good.type }}
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import ModalWindowButtonClose from "./ModalWindowButtonClose.vue";

export default {
  props: {
    tender_info: Object,
  },

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
<style>
.custom-scrollbar {
  scrollbar-width: thin;
  scrollbar-color: #535353 #272727;
}

.custom-scrollbar::-webkit-scrollbar {
  width: 5px;
}

.custom-scrollbar::-webkit-scrollbar-track {
  background: #27272700;
}

.custom-scrollbar::-webkit-scrollbar-thumb {
  background-color: #535353;
  border-radius: 12px;
}

.custom-scrollbar::-webkit-scrollbar-thumb:hover {
  background-color: #323232;
}
</style>
