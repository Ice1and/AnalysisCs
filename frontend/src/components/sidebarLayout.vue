<script setup>
    import { defineProps, ref, onMounted, onUnmounted } from 'vue'


    const props = defineProps({
        items: {
            type: Array,
            required: true
        },
        logo: {
            type: String,
            required: true
        },
        logoName: {
            type: String,
            required: true
        }
    })

    const selectButton = ref(null)

    const toggleIsOpen = ref(false)

    const screenWidth = ref(window.innerWidth)

    const updateScreenWidth = () => {
        screenWidth.value = window.innerWidth
        if (screenWidth.value >= 1024) {
            toggleIsOpen.value = false
        }
    }

    const switchToggleStatus = () => {
        toggleIsOpen.value = !toggleIsOpen.value
    }

    onMounted(() => {
        window.addEventListener('resize', updateScreenWidth)
        updateScreenWidth()
    })

    onUnmounted(() => {
        window.removeEventListener('resize', updateScreenWidth)
    })
</script>

<template>
    <div class="relative min-h-svh w-full isolate-auto bg-white lg:bg-zinc-100 flex max-lg:flex-col">
        <!-- sidebar -->
        <!-- fixed 使 nav 脱离文档流 -->
        <nav class="fixed flex flex-col inset-y-0 left-0 w-64 max-lg:hidden">
            <div class="flex flex-col p-4 border-b border-zinc-200 box-border">
                <button @click="selectButton = null" class="flex gap-3 items-center p-2">
                    <span class="size-7 shrink-0 rounded-full *:rounded-full">
                        <img class="size-full" :src="props.logo" alt="logo">
                    </span>
                    <span class="truncate">{{ props.logoName }}</span>
                </button>
            </div>
            <div class="flex flex-1 flex-col p-4 overflow-y-auto">
                <div class="flex flex-col gap-1.25">
                    <button
                        :class="[
                            'flex w-full text-left text-sm p-2 gap-3 items-center rounded-lg select-none cursor-pointer',
                            selectButton === item.name
                            ? 'outline-1 outline-zinc-200 bg-white'
                            : 'hover:bg-gray-950/5'
                        ]"
                        v-for="item in props.items"
                        :key="item.name"
                        @click="selectButton = item.name"
                    >
                        <span class="material-symbols-outlined" style="font-size: 22px;">{{ item.name }}</span>
                        <span class="truncate">{{ item.tooltip }}</span>
                    </button>
                </div>
            </div>
        </nav>

        <!-- 屏幕宽度小于 lg 时生效 header 汉堡按钮 -->
        <header class="flex px-4 items-center lg:hidden">
            <div class="py-2.5">
                <button @click="switchToggleStatus" class="flex p-2 text-zinc-400 hover:text-gray-800 hover:bg-gray-950/5 rounded-lg select-none cursor-pointer">
                    <span class="material-symbols-outlined" style="font-size: 22px;">menu</span>
                </button>
            </div>
        </header>

        <!-- main -->
        <main class="lg:pr-2 lg:pt-2 lg:pb-2 lg:pl-64 lg:min-w-0 flex flex-1">
            <div class="flex-1 p-6 bg-white lg:border-1 lg:border-zinc-200 lg:rounded-lg lg:p-10 box-border">
                <div class="mx-auto max-w-6xl w-full h-full">
                    <slot></slot>
                </div>
            </div>
        </main>

        <!-- 垂直导航，当 toggleIsOpen 为 true 且屏幕宽度小于 lg 时生效 -->
        <div class="lg:hidden">
            <Transition
                enter-active-class="transition-opacity duration-300 ease-in-out"
                leave-active-class="transition-opacity duration-300 ease-in-out"
                enter-from-class="opacity-0"
                leave-to-class="opacity-0"
            >
                <div v-if="toggleIsOpen" @click="switchToggleStatus" class="fixed isolate-auto inset-0 bg-black/30"></div>
            </Transition>

            <Transition
                enter-active-class="transition-transform duration-300 ease-in-out"
                leave-active-class="transition-transform duration-300 ease-in-out"
                enter-from-class="-translate-x-full"
                leave-to-class="-translate-x-full"
            >
                <div v-if="toggleIsOpen" class="fixed inset-y-0 max-w-80 w-full p-2">
                    <div class="flex flex-col h-full bg-white rounded-lg ring-1 ring-zinc-950/5">
                        <div class="px-4 pt-3">
                            <button @click="switchToggleStatus" class="flex p-2 text-zinc-500 hover:text-gray-800 hover:bg-gray-950/5 rounded-lg select-none cursor-pointer">
                                <span class="material-symbols-outlined" style="font-size: 22px">close</span>
                            </button>
                        </div>

                        <nav class="flex flex-col h-full min-h-0">
                            <div class="flex flex-col p-4 border-b border-zinc-950/5 box-border">
                                <button class="flex gap-3 items-center p-2">
                                    <span class="size-7 shrink-0 rounded-full *:rounded-full">
                                        <img class="size-full" :src="props.logo" alt="logo">
                                    </span>
                                    <span class="truncate">{{ props.logoName }}</span>
                                </button>
                            </div>
                            <div class="flex flex-1 flex-col p-4 overflow-y-auto">
                                <div class="flex flex-col gap-1.25">
                                    <button class="flex w-full text-left text-sm p-2 gap-3 items-center rounded-lg select-none hover:bg-gray-950/5 cursor-pointer"
                                        v-for="item in props.items"
                                        :key="item.name"
                                    >
                                        <span class="material-symbols-outlined" style="font-size: 22px;">{{ item.name }}</span>
                                        <span class="truncate">{{ item.tooltip }}</span>
                                    </button>
                                </div>
                            </div>
                        </nav>
                    </div>
                </div>
            </Transition>
        </div>

    </div>
</template>

<style scoped>
</style>