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
          <p class="text-activeText text-xl font-bold text-center">Архив</p>
          <div class="flex flex-col gap-3 border-neutral-600 duration-500 pt-4">
            <!-- Ключевые слова -->
            <div class="flex items-start w-full">
              <p class="text-activeText w-1/6">Ключевые слова</p>
              <input
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
            <div class="flex items-center w-full">
              <p class="text-activeText w-1/6">Ценовой диапазон</p>
              <input
                type="number"
                min="0"
                step="1"
                class="rounded-md w-1/6 h-10 placeholder:pl-2.5 text-center placeholder:text-sm border-[1px] border-neutral-300 shadow-sm"
                placeholder="0 руб."
              />
              <div class="pl-1">
                <svg
                  fill="currentColor"
                  viewBox="0 0 24 24"
                  xmlns="http://www.w3.org/2000/svg"
                  class="w-5 h-5 text-neutral-100 duration-300"
                >
                  <path
                    id="primary"
                    d="M14,11H9V3h5a4,4,0,0,1,4,4h0A4,4,0,0,1,14,11ZM9,3V21M6,11H9"
                    :style="{ stroke: isDarkMode ? 'white' : '#a0a0a0' }"
                    style="
                      fill: none;
                      stroke-linecap: round;
                      stroke-linejoin: round;
                      stroke-width: 2;
                    "
                  ></path>
                  <line
                    id="primary-2"
                    data-name="primary"
                    x1="6"
                    y1="15"
                    x2="15"
                    y2="15"
                    :style="{ stroke: isDarkMode ? 'white' : '#a0a0a0' }"
                    style="
                      fill: none;
                      stroke-linecap: round;
                      stroke-linejoin: round;
                      stroke-width: 2;
                    "
                  ></line>
                </svg>
              </div>
              <p class="text-activeText px-4">—</p>

              <input
                class="rounded-md w-1/6 h-10 placeholder:pl-2.5 text-center placeholder:text-sm border-[1px] border-neutral-300 shadow-sm"
                type="number"
                min="0"
                step="1"
                placeholder="0 руб."
              />
              <div class="pl-1">
                <svg
                  fill="currentColor"
                  viewBox="0 0 24 24"
                  xmlns="http://www.w3.org/2000/svg"
                  class="w-5 h-5 text-neutral-100 duration-300"
                >
                  <path
                    id="primary"
                    d="M14,11H9V3h5a4,4,0,0,1,4,4h0A4,4,0,0,1,14,11ZM9,3V21M6,11H9"
                    :style="{ stroke: isDarkMode ? 'white' : '#a0a0a0' }"
                    style="
                      fill: none;
                      stroke-linecap: round;
                      stroke-linejoin: round;
                      stroke-width: 2;
                    "
                  ></path>
                  <line
                    id="primary-2"
                    data-name="primary"
                    x1="6"
                    y1="15"
                    x2="15"
                    y2="15"
                    :style="{ stroke: isDarkMode ? 'white' : '#a0a0a0' }"
                    style="
                      fill: none;
                      stroke-linecap: round;
                      stroke-linejoin: round;
                      stroke-width: 2;
                    "
                  ></line>
                </svg>
              </div>
            </div>
            <!-- Дата -->
            <div class="flex items-center w-full">
              <p class="text-activeText w-1/6">Период публикации</p>
              <div class="w-4/6">
                <VueDatePicker
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
          <TenderCard v-for="el in 10" />
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
import "@vuepic/vue-datepicker/dist/main.css";
export default {
  components: {
    AssistantCategoryService,
    BaseIcon,
    AssistantCategoryServiceSection,
    SidebarMain,
    TenderCard,
    VueDatePicker,
  },

  data() {
    return {
      questionQuery: "",
      date: null,
    };
  },

  methods: {
    askQuestion() {
      console.log(this.questionQuery);
      axios
        .post(
          `http://${process.env.VUE_APP_ASSISTANT_SEARCH_IP}/assistant/llamaSupportStream?text=${this.questionQuery}`,
          { responseType: "stream" }
        )
        .then((response) => {
          console.log(response.data);
        });
    },
  },

  computed: {
    isDarkMode() {
      return this.$store.state.darkMode;
    },
  },
};
</script>
<style>
.rainbows {
  position: relative;
}

@keyframes rainbow {
  0% {
    color: white;
  }

  33% {
    color: blue;
  }

  66% {
    color: red;
  }

  100% {
    color: white;
  }
}

.owl {
  position: absolute;
  width: 40px;
  height: 40px;
  background-image: url("https://freesvg.org/img/1531730612.png");
  background-size: cover;
  animation: fly-around 5s ease-in-out infinite;
}

@keyframes fly-around {
  0% {
    left: 40px;
    top: 0px;
  }

  25% {
    left: 40px;
    top: 20px;
  }

  50% {
    left: 55px;
    top: 5px;
  }

  75% {
    left: 25;
    top: 15px;
  }

  100% {
    left: 40px;
    top: 0px;
  }
}

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
