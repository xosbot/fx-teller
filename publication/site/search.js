(async function() {
    const input = document.getElementById('search-input');
    const results = document.getElementById('search-results');
    if (!input) return;

    let index = null;

    async function loadIndex() {
        if (!index) {
            const res = await fetch('/search-index.json');
            index = await res.json();
        }
        return index;
    }

    function escapeHtml(s) {
        return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    }

    function score(query, doc) {
        const q = query.toLowerCase();
        const title = (doc.title || '').toLowerCase();
        const summary = (doc.summary || '').toLowerCase();
        let s = 0;
        if (title.includes(q)) s += 10;
        if (summary.includes(q)) s += 5;
        const titleWords = title.split(/\s+/);
        const qWords = q.split(/\s+/);
        for (const qw of qWords) {
            if (title.includes(qw)) s += 3;
            if (summary.includes(qw)) s += 1;
        }
        return s;
    }

    async function doSearch(query) {
        if (!query || query.length < 2) {
            results.innerHTML = '<p class="lead">Type at least 2 characters to search.</p>';
            return;
        }
        const data = await loadIndex();
        const matched = data.docs
            .map(d => ({ ...d, _score: score(query, d) }))
            .filter(d => d._score > 0)
            .sort((a, b) => b._score - a._score)
            .slice(0, 30);

        if (matched.length === 0) {
            results.innerHTML = '<p class="lead">No matches found.</p>';
            return;
        }

        results.innerHTML = matched.map(d => `
            <a href="${d.url}/" class="search-result" style="text-decoration:none;display:block;">
                <h4>${escapeHtml(d.title)}</h4>
                <p>${escapeHtml(d.summary.substring(0, 200))}${d.summary.length > 200 ? '…' : ''}</p>
                <div class="doc-card-meta">${escapeHtml(d.folder || '')}</div>
            </a>
        `).join('');
    }

    let debounceTimer;
    input.addEventListener('input', () => {
        clearTimeout(debounceTimer);
        debounceTimer = setTimeout(() => doSearch(input.value.trim()), 150);
    });

    results.innerHTML = '<p class="lead">Start typing to search across the entire knowledge base.</p>';
})();
