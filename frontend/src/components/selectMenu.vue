<script setup>
    import { ref, defineEmits } from 'vue'

    const emit = defineEmits(['selectedDate'])
    const handleSelect = (event) => {
        emit('selectedDate', event.target.value.toLowerCase())
    }

    const selectItems = ref([
        {value: 'Last day', days: 1},
        {value: 'Last week', days: 7},
        {value: 'Last month', days: 30}
    ])

</script>

<template>
    <span class="group relative block w-full">
        <select
            name="period"
            id=""
            class="relative block w-full appearance-none rounded-lg py-[5px] pl-3 pr-9 text-base/6 text-zinc-950 shadow-xs placeholder:text-zinc-500 sm:text-sm/6 border border-zinc-950/10 hover:border-zinc-950/20 focus:outline-none bg-transparent [&_optgroup]:font-semibold"
            @change="handleSelect"
        >
            <option v-for="selectItem in selectItems" :value="selectItem.value">{{ selectItem.value }}</option>
        </select>
        <span class="pointer-events-none absolute inset-y-0 right-0 flex items-center pr-2">
            <svg class="size-5 stroke-zinc-500 group-has-data-disabled:stroke-zinc-600 sm:size-4 dark:stroke-zinc-400 forced-colors:stroke-[CanvasText]" viewBox="0 0 16 16" aria-hidden="true" fill="none"><path d="M5.75 10.75L8 13L10.25 10.75" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path><path d="M10.25 5.25L8 3L5.75 5.25" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></svg>
        </span>
    </span>
</template>