<script lang="ts">
    import { fly, fade } from 'svelte/transition';
    import { onMount } from 'svelte';
    import { marked } from 'marked';
    import ApiRequest from '$lib/ApiRequest.svelte';

    interface ModelType {
        id: string;
        name: string;
        description: string;
    }

    const MODEL_TYPES: ModelType[] = [
        { id: 'text', name: 'LLM (llm for text)', description: 'Text-based models for natural language processing' },
        { id: 'image', name: 'VLM (llm for image)', description: 'Image processing and analysis models' }
    ];

    let selectedModel = $state('');
    let modelUrl = $state('http://localhost:8000');
    let prompt = $state('');
    let uploadedImage = $state<File | null>(null);
    let responseText = $state('');
    let showMarkdown = $state(false);
    let show = $state(false);
    let modelName = $state('');
    let isLoading = $state(false);

    function toggleMarkdown() {
        showMarkdown = !showMarkdown;
    }

    onMount(() => {
        show = true;    
    }); 

    function handleImageUpload(event: Event) {
        const target = event.target as HTMLInputElement;
        const file = target.files?.[0];
        if (file) {
            uploadedImage = file;
        }
    }

    // Response callback 함수
    function handelResponseText(text: string) {
        responseText = text;
        isLoading = false;
    }

    function clearResponse() {
        responseText = '';
    }

    async function handleSubmit() {
        if (!prompt.trim() || isLoading) return;
        
        isLoading = true;
        responseText = '';
        

    }
</script>

{#if show}
<div class="min-h-screen bg-gradient-to-br from-slate-50 to-blue-50 p-4 sm:p-6 md:p-8">
    <div class="max-w-4xl mx-auto">
        <header class="text-center mb-8">
            <h1 in:fly={{ y: 300, duration: 1000, delay: 150 }} class="text-4xl md:text-5xl font-bold bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent mb-2">LLM Tester</h1>
            <p in:fly={{ y: 200, duration: 1000, delay: 700 }} class="text-lg text-slate-600 max-w-2xl mx-auto">LLM 모델 테스트</p>
        </header>
        <!-- 중간 박스 -->
        <div in:fly={{ y: 300, duration: 1000, delay: 150 }} class="bg-white/80 backdrop-blur-sm rounded-2xl shadow-2xl p-6 space-y-6 border border-slate-100">
            <div>
                <label for="model-type" class="block text-sm font-medium text-slate-700 mb-2">Model Type</label>
                <select
                    bind:value={selectedModel}
                    id="model-type"
                    class="block w-full px-4 py-3 text-slate-700 bg-white border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200 outline-none"
                >
                    {#each MODEL_TYPES as model}
                        <option value={model.id}>{model.name}</option>
                    {/each}
                </select>
                <p class="mt-1 text-sm text-slate-500">{MODEL_TYPES.find((model) => model.id === selectedModel)?.description}</p>
            </div>
            <label for="model-url" class="block text-sm font-medium text-gray-700 mb-2">Model API URL</label>
            <div class="relative">
                <input
                    type="text"
                    id="model-url"
                    bind:value={modelUrl}
                    placeholder="Enter model API URL"
                    class="block w-full px-4 py-3 text-slate-700 bg-white border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200 outline-none"
                />
                <button
                    type="button"
                    class="absolute right-1 top-1/2 -translate-y-1/2 px-4 py-2 text-sm font-medium text-white bg-gradient-to-r from-blue-500 to-indigo-600 rounded-xl hover:opacity-90 transition-all duration-200 shadow-md hover:shadow-lg active:scale-95"
                    onclick={(e) => { e.preventDefault(); modelUrl = 'http://localhost:17000'; }}
                >
                    Default
                </button>
            </div>
            <label for="model-name" class="block text-sm font-medium text-gray-700 mb-2">Model Name</label>
            <div class="relative">
                <input
                    type="text"
                    id="model-name"
                    bind:value={modelName}
                    placeholder="Enter model name"
                    class="block w-full px-4 py-3 text-slate-700 bg-white border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200 outline-none"
                />
            </div>
            <!-- 이미지 업로드 컴포넌트 (이미지 모델 선택 시만 표시) -->
            {#if selectedModel === 'image'}
                <div>
                    <label for="image-upload" class="block text-sm font-medium text-slate-700 mb-2">Upload Image</label>
                    <div class="flex flex-col sm:flex-row gap-4 items-start sm:items-center">
                        <div class="w-full">
                            <div class="flex items-center justify-center w-full">
                                <label for="image-upload" class="flex flex-col items-center justify-center w-full h-32 border-2 border-slate-200 border-dashed rounded-2xl cursor-pointer bg-slate-50 hover:bg-slate-100 transition-colors duration-200">
                                    <div class="flex flex-col items-center justify-center pt-5 pb-6">
                                        <svg class="w-8 h-8 mb-2 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12"></path>
                                        </svg>
                                        <p class="mb-1 text-sm text-slate-500">
                                            <span class="font-semibold">Click to upload</span> or drag and drop
                                        </p>
                                        <p class="text-xs text-slate-400">PNG, JPG, JPEG (MAX. 5MB)</p>
                                    </div>
                                    <input id="image-upload" type="file" class="hidden" accept="image/*" onchange={handleImageUpload} />
                                </label>
                            </div>
                        </div>
                        {#if uploadedImage}
                            <div class="flex-shrink-0">
                                <div class="relative group">
                                    <img
                                        src={URL.createObjectURL(uploadedImage)}
                                        alt="Preview"
                                        class="w-24 h-24 object-cover rounded-xl shadow-md group-hover:shadow-lg transition-shadow duration-200"
                                    />
                                    <button
                                        type="button"
                                        class="absolute -top-2 -right-2 bg-red-500 text-white rounded-full p-1 opacity-0 group-hover:opacity-100 transition-opacity duration-200"
                                        onclick={(e) => { e.preventDefault(); uploadedImage = null; }}
                                        aria-label="Remove image"
                                    >
                                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                                        </svg>
                                    </button>
                                </div>
                            </div>
                        {/if}
                    </div>
                </div>
            {/if}

            <div class="space-y-2">
                <div class="flex items-center justify-between">
                    <label for="prompt" class="block text-sm font-medium text-slate-700">Prompt</label>
                    <div class="flex items-center space-x-2">
                        <label class="relative inline-flex items-center cursor-pointer">
                            <input type="checkbox" bind:checked={showMarkdown} class="sr-only peer">
                            <div class="w-11 h-6 bg-slate-200 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-slate-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-blue-600"></div>
                            <span class="ml-2 text-sm font-medium text-slate-700">Markdown</span>
                        </label>
                    </div>
                </div>
                <div class="relative">
                    <textarea
                        id="prompt"
                        bind:value={prompt}
                        placeholder="Enter your prompt here..."
                        rows="4"
                        class="block w-full px-4 py-3 text-slate-700 bg-white border border-slate-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all duration-200 outline-none resize-none"
                        onkeydown={(e) => {
                            if (e.key === 'Enter' && !e.shiftKey) {
                                e.preventDefault();
                                handleSubmit();
                            }
                        }}
                    ></textarea>
                </div>
            </div>
            {#if responseText}
                <div class="mt-6">
                    <div class="flex items-center justify-between mb-2">
                        <h2 class="text-lg font-medium text-slate-800">Response</h2>
                        <button
                            type="button"
                            class="text-slate-400 hover:text-slate-600 transition-colors duration-200"
onclick={(e) => { e.preventDefault(); clearResponse(); }}
                            aria-label="Clear response"
                        >
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                                <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd" />
                            </svg>
                        </button>
                    </div>
                    {#if showMarkdown}
                    <!-- <div class="bg-white/80 backdrop-blur-sm rounded-2xl p-6 border border-slate-100 overflow-auto max-h-96"> -->
                    <div class="prose prose-slate dark:prose-invert
                        bg-white/80 backdrop-blur-sm rounded-2xl p-6
                        border border-slate-100 overflow-auto max-h-96
                        [&_table]:border [&_table]:border-slate-200 [&_table]:rounded-lg
                        [&_th]:bg-slate-50 [&_th]:px-4 [&_th]:py-3 [&_th]:text-left [&_th]:text-sm [&_th]:font-medium [&_th]:text-slate-700 [&_th]:border-b [&_th]:border-slate-200
                        [&_td]:px-4 [&_td]:py-3 [&_td]:text-sm [&_td]:text-slate-700 [&_td]:border-b [&_td]:border-slate-100
                        [&_tr:last-child_td]:border-0">
                    {@html marked(responseText)}
                    </div>
                    {:else}
                        <pre class="whitespace-pre-wrap font-sans">{responseText}</pre>
                    {/if}
                </div>
            {/if}

            <div class="mt-6">
                <ApiRequest 
                    modelUrl={modelUrl}
                    prompt={prompt}
                    uploadedImage={uploadedImage}
                    selectedModel={selectedModel}
                    onResponse={handelResponseText}
                    modelName={modelName}
                />
            </div>
        </div>
    </div>
</div>
{/if}
