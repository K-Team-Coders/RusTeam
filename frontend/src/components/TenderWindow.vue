<template>
  <div class="flex w-full justify-center p-6 gap-4 duration-500 min-h-[98vh]">
    <div class="fixed w-64 left-6">
      <SidebarMain />
    </div>
    <div
      class="ml-72 w-full bg-frameBackground rounded-md border-[0.5px] duration-500"
    >
      <div class="h-full p-4">
        <!-- Блок поиска -->
        <div class="">
          <p class="text-activeText text-xl font-bold text-center">Поиск</p>
          <div class="flex flex-col gap-3 border-neutral-600 duration-500 pt-4">
            <!-- Ключевые слова -->
            <div class="flex items-start w-full">
              <p class="text-activeText w-1/6">Ключевое слово</p>
              <input
                v-model="keyword"
                class="rounded-md w-4/6 h-12 pl-2.5 placeholder:text-sm border-[1px] border-neutral-300 shadow-sm"
                placeholder="Например: сталь, 36.40.11.133"
              />
            </div>
            <!-- Исключить слова -->
            <div class="flex items-center w-full">
              <p class="text-activeText w-1/6">Исключить слова</p>
              <input
                class="rounded-md pl-2.5 w-4/6 h-8 border-[1px] text-sm border-neutral-300 shadow-sm"
                placeholder="Введите слова-исключения"
              />
            </div>
            <!-- Цена -->

            <!-- Дата -->
            <div class="flex items-center w-full">
              <p class="text-activeText w-1/6">Период публикации</p>
              <div class="w-4/6">
                <VueDatePicker
                  day-picker
                  v-model="date"
                  range
                  multi-calendars
                  text-input
                  placeholder="Напишите или выберите период..."
                  locale="ru"
                />
              </div>
            </div>
            <!-- Кнопка найти -->
            <div class="flex pt-3">
              <button
                @click.prevent="searchTender()"
                type="button"
                class="text-activeText px-5 py-2 rounded-md bg-blue-700 text-neutral-100 shadow-sm hover:bg-blue-900 duration-300"
              >
                Найти
              </button>
            </div>
          </div>
        </div>
        <hr class="h-px my-8 bg-gray-300" />
        <!-- Всего тендеров найдено и сортировка -->
        <div class="flex items-center">
          <p class="text-neutral-400 text-sm">125 300 закупок</p>
          <select
            name="pets"
            class="rounded-md px-2 py-1 ml-4 text-sm border-2 border-neutral-300 shadow-sm"
          >
            <option value="">По дате публикации (убыв.)</option>
            <option value="">По дате публикации (возр.)</option>
            <option value="">По релевантоности</option>
            <option value="">По окончанию подачи заявок</option>
            <option value="">По дате планируемой публикации</option>
            <option value="">По НМЦ</option>
          </select>
        </div>
        <!-- Карточки найденных тендеров -->
        <div class="pt-2">
          <LoaderBig v-if="isLoading" />
          <TenderCard
            v-else
            :tender_info="tender"
            v-for="tender in tenders_info"
            :key="tender"
          />
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import AssistantCategoryService from "./AssistantCategoryService.vue";
import AssistantCategoryServiceSection from "./AssistantCategoryServiceSection.vue";
import BaseIcon from "./BaseIcon.vue";
import SidebarMain from "./SidebarMain.vue";
import TenderCard from "./TenderCard.vue";
import VueDatePicker from "@vuepic/vue-datepicker";
import LoaderBig from "./LoaderBig.vue";
import "@vuepic/vue-datepicker/dist/main.css";

export default {
  components: {
    AssistantCategoryService,
    BaseIcon,
    AssistantCategoryServiceSection,
    SidebarMain,
    TenderCard,
    VueDatePicker,
    LoaderBig,
  },

  data() {
    return {
      keyword: "",
      date: null,
      isLoading: false,
      tenders_info: [],
    };
  },

  methods: {
    searchTender() {
      this.isLoading = true;
      let post_data = {
        element: this.keyword,
        date_1: this.timestampToDate_created,
        date_2: this.timestampToDate_finished,
      };
      console.log(post_data);
      axios
        .post(
          `http://${process.env.VUE_APP_SEARCH_TENDER_SERVICE_IP}/parse_tenderpro?element=${this.keyword}&date_1=${this.timestampToDate_created}&date_2=${this.timestampToDate_finished}'`
        )
        .then((response) => {
          console.log(response.data);
          this.tenders_info = response.data;
          this.isLoading = false;
        });
    },
    datetimeToDate(datetime) {
      const date = new Date(datetime);
      const day = date.getDate().toString().padStart(2, "0");
      const month = (date.getMonth() + 1).toString().padStart(2, "0");
      const year = date.getFullYear();
      const formattedDate = `${day}.${month}.${year}`;
      console.log(formattedDate);
      return formattedDate;
    },
  },

  computed: {
    isDarkMode() {
      return this.$store.state.darkMode;
    },
    timestampToDate_created() {
      return this.datetimeToDate(this.date[0]);
    },
    timestampToDate_finished() {
      return this.datetimeToDate(this.date[1]);
    },
  },
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
