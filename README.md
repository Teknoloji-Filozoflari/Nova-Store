# Nova-Store

Signed, PR-reviewed application catalog for
[Nova](https://github.com/Teknoloji-Filozoflari/Nova).

Contributors add apps here; Nova fetches **signed** release artifacts only and
falls back to the last trusted catalog if verification fails.

**519 apps** across 18 categories · Trust A 401 · B 7 · C 88 · D 23

> Catalog entries below are generated from `apps/**/*.toml` (name, short
> description, upstream link). Install methods and trust classes live in those
> TOML files — this README is a browsable index, not a second source of truth.

## Table of contents

| Category | Apps | Focus |
|----------|-----:|-------|
| [AI](#ai) | 25 | Terminal LLM clients, coding agents, and AI CLIs. |
| [Git](#git) | 20 | Git TUIs, diff tools, and VCS helpers. |
| [Dosya ve Arama](#files) | 41 | Finders, fuzzy selectors, file managers, and search. |
| [Geliştirme](#development) | 67 | HTTP clients, JSON tools, language CLIs, and developer utilities. |
| [Editörler](#editors) | 22 | Terminal editors and modal text editing tools. |
| [Sistem](#system) | 32 | Process monitors, disk tools, and host observability. |
| [Paneller](#panels) | 21 | Dashboards and system overview panels. |
| [Ağ](#networking) | 32 | DNS, bandwidth, traceroute, and network diagnostics. |
| [Konteyner](#containers) | 37 | Docker, Kubernetes, and container inspection tools. |
| [Veritabanı](#database) | 19 | Database CLIs, TUI clients, and query helpers. |
| [Güvenlik](#security) | 25 | Crypto, secrets, scanners, and signing tooling. |
| [Medya](#media) | 18 | Audio, video, and image terminal tools. |
| [Mesajlaşma](#messaging) | 21 | IRC, Matrix, and chat terminal clients. |
| [Verimlilik](#productivity) | 31 | Terminal multiplexers, notes, backup, and workflow helpers. |
| [Oyunlar](#games) | 26 | Terminal games and playful diversions. |
| [Ekran Koruyucular](#screensavers) | 11 | ASCII / terminal screensaver animations. |
| [Web](#web) | 12 | Text-mode browsers and web fetch helpers. |
| [Günlük](#daily) | 59 | Everyday utilities and general-purpose CLIs. |

## Trust classes

| Class | Meaning |
|-------|---------|
| **A** | Distro / official package manager (`apt`/`dnf`/`pacman`/`brew`) |
| **B** | Project official binary (`download_archive`, signature preferred) |
| **C** | Registry (`cargo`/`npm`/`pipx`/`uv`) — requires `risk_note` |
| **D** | Manual docs only |

Arch hosts: prefer `pacman` when the package exists in official repos.

## Catalog

<a id="ai"></a>

### AI

Terminal LLM clients, coding agents, and AI CLIs.

| App | Description | Trust | Install |
|-----|-------------|:-----:|---------|
| [aichat](https://github.com/sigoden/aichat) | Çok modellı AI CLI sohbet aracı. | C | `cargo` |
| [Aider](https://aider.chat) | Terminalde LLM ile çift programlama; Claude ve GPT ile kod düzenler. | C | `pipx` |
| [Amp](https://ampcode.com) | Sourcegraph'in terminal odaklı AI kodlama ajanı. | C | `npm` |
| [Auggie](https://www.augmentcode.com/) | Augment Code terminal asistanı. | C | `npm` |
| [chatgpt-cli](https://github.com/kardolus/chatgpt-cli) | Basit ChatGPT komut satırı istemcisi. | D | `manual` |
| [Claude Code](https://code.claude.com) | Anthropic'in terminal tabanlı kodlama asistanı. | C | `npm` |
| [Codex](https://github.com/openai/codex) | OpenAI'nin terminal tabanlı kodlama ajanı. | C | `npm` |
| [Continue CLI](https://continue.dev) | Continue.dev açık kaynak kod asistanının CLI istemcisi. | C | `npm` |
| [Crush](https://github.com/charmbracelet/crush) | Charmbracelet'in terminal AI kodlama ajanı. | A | `brew` |
| [Fabric](https://github.com/danielmiessler/fabric) | AI örüntüleri ile içerik işleme CLI. | A | `pacman` |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | Google Gemini için resmi terminal kodlama istemcisi. | C | `npm` |
| [Goose](https://block.github.io/goose/) | Block'un açık kaynaklı, yerel çalışabilen AI ajanı. | D | `manual` |
| [llm](https://llm.datasette.io) | Simon Willison'ın çok modellli komut satırı LLM aracı. | C | `pipx` |
| [llmfit](https://github.com/AlexsJones/llmfit) | Donanıma göre hangi yerel LLM modellerinin çalışacağını önerir (TUI). | A | `pacman` |
| [mods](https://github.com/charmbracelet/mods) | CLI için AI (Charmbracelet). | A | `pacman` |
| [oh-my-pi](https://github.com/can1357/oh-my-pi) | omp (oh-my-pi), Stencil Labs’ın Pi tabanlı terminal kodlama ajanıdır: 60+ model sağlayıcısı, 31+ yerleşik araç, LSP ve gerçek hata ayıklayıcı (DAP) desteği sunar. Dosya okuma/düzenleme, alt ajanlar, kod çalıştırma ve işbirliği oturumları içerir. Nova bir mağaza/başlatıcıdır; oh-my-pi projede kod yazıp düzenleyen ajanın kendisidir. | D | `manual` |
| [Ollama](https://ollama.com/) | Yerel LLM çalıştırma ve yönetme. | A | `pacman` |
| [OpenCode](https://opencode.ai) | Terminalde çalışan açık kaynaklı yapay zekâ kodlama asistanı. | C | `npm` |
| [OpenHands](https://github.com/All-Hands-AI/OpenHands) | Açık kaynak AI yazılım mühendisi ajanı. | C | `pipx` |
| [Plandex](https://github.com/plandex-ai/plandex) | Büyük kod tabanları için terminal AI geliştirme aracı. | D | `manual` |
| [Qwen Code](https://github.com/QwenLM/qwen-code) | Alibaba Qwen modelleri için terminal kodlama istemcisi. | C | `npm` |
| [ShellGPT](https://github.com/TheR1D/shell_gpt) | ChatGPT destekli kabuk asistanı (sgpt). | C | `pipx` |
| [tgpt](https://github.com/aandrew-me/tgpt) | ChatGPT benzeri terminal AI istemcisi. | A | `pacman` |
| [tts](https://github.com/coqui-ai/TTS) | Coqui TTS komut satırı ses sentezi. | C | `pipx` |
| [VT Code](https://github.com/vinhnx/vtcode) | Yerel öncelikli terminal AI kodlama ajanı (CLI). | A | `brew` |

<a id="git"></a>

### Git

Git TUIs, diff tools, and VCS helpers.

| App | Description | Trust | Install |
|-----|-------------|:-----:|---------|
| [delta](https://github.com/dandavison/delta) | Git diff'lerini renkli ve okunaklı gösterir; genellikle git yapılandırmasına bağlanır. | A | `apt` |
| [difftastic](https://difftastic.wilfred.me.uk/) | Sözdizimi bilen yapısal diff aracı (difft). | A | `pacman` |
| [ggc](https://github.com/bmf-san/ggc) | Geleneksel komutlar ve TUI sunan modern Git CLI. | A | `brew` |
| [gh-dash](https://github.com/dlvhdr/gh-dash) | GitHub PR ve issue'ları için zengin terminal panosu. | D | `manual` |
| [Git Town](https://github.com/git-town/git-town) | Git Town, özellik dallarının oluşturma, senkron, PR önerme, birleştirme ve temizleme adımlarını otomatikleştiren Git komut setidir. Git Flow, GitHub/GitLab Flow ve trunk-based iş akışlarıyla uyumludur; mono-repo ve yığılmış (stacked) değişiklikleri destekler. hack/sync/propose/ship ile çakışma sonrası continue/undo sunar. Nova depo yaşam döngüsü yönetmez; Git Town dal iş akışını hızlandırır. | A | `pacman` |
| [git-absorb](https://github.com/tummychow/git-absorb) | Otomatik fixup commit emici. | A | `pacman` |
| [git-cliff](https://github.com/orhun/git-cliff) | Changelog üretici. | A | `pacman` |
| [git-lfs](https://git-lfs.com/) | Git Large File Storage. | A | `pacman` |
| [GitHub CLI](https://cli.github.com/) | GitHub için resmi komut satırı aracı (PR, issue, Actions). | A | `apt` |
| [gitoxide](https://github.com/Byron/gitoxide) | Rust ile yazılmış hızlı Git uygulaması (gix). | A | `pacman` |
| [gitu](https://github.com/altsem/gitu) | Magit esinli TUI Git istemcisi. | A | `pacman` |
| [gitui](https://github.com/extrawurst/gitui) | Rust ile yazılmış hızlı Git terminal arayüzü. | A | `apt` |
| [glab](https://gitlab.com/gitlab-org/cli) | GitLab resmi CLI. | A | `pacman` |
| [jj](https://github.com/jj-vcs/jj) | Jujutsu: Git uyumlu, basit ve güçlü sürüm kontrol sistemi. | A | `pacman` |
| [lazygit](https://github.com/jesseduffield/lazygit) | Git işlemleri için klavye odaklı terminal arayüzü. | B | `download_archive` |
| [onefetch](https://github.com/o2sh/onefetch) | Git deposu özetini terminalde gösteren araç. | A | `pacman` |
| [serie](https://github.com/lusingander/serie) | Zengin git commit grafiği gösteren terminal aracı. | A | `pacman` |
| [soft-serve](https://github.com/charmbracelet/soft-serve) | Komut satırı için self-host Git sunucusu (Charm). | A | `pacman` |
| [tea](https://gitea.com/gitea/tea) | Gitea CLI. | A | `pacman` |
| [tig](https://jonas.github.io/tig/) | ncurses tabanlı metin kipinde Git arayüzü. | A | `apt` |

<a id="files"></a>

### Dosya ve Arama

Finders, fuzzy selectors, file managers, and search.

| App | Description | Trust | Install |
|-----|-------------|:-----:|---------|
| [bat](https://github.com/sharkdp/bat) | Sözdizimi renklendirmeli dosya görüntüleyici. | A | `apt` |
| [broot](https://github.com/Canop/broot) | Dizin ağacını etkileşimli gezen dosya gezgini. | C | `cargo` |
| [clifm](https://github.com/leo-arch/clifm) | Komut satırı dosya yöneticisi. | A | `pacman` |
| [dust](https://github.com/bootandy/dust) | Disk kullanımını ağaç olarak gösteren du alternatifi. | C | `cargo` |
| [eza](https://github.com/eza-community/eza) | Renkli ve simgeli dizin listesi; `ls`ye modern alternatif. | B | `download_archive` |
| [far2l](https://github.com/elfmz/far2l) | Far Manager Linux portu. | A | `pacman` |
| [fd](https://github.com/sharkdp/fd) | Kullanıcı dostu, hızlı dosya bulucu; find alternatifi. | A | `apt` |
| [fdupes](https://github.com/adrianlopezroche/fdupes) | Yinelenen dosya bulucu. | A | `pacman` |
| [felix](https://github.com/kyoheiu/felix) | Vim tuş bağlamalı TUI dosya yöneticisi. | A | `pacman` |
| [fff](https://github.com/dylanaraps/fff) | Basit ve hızlı dosya yöneticisi. | A | `pacman` |
| [fzf](https://github.com/junegunn/fzf) | Bulanık arama aracı; tek başına çalışır, Ctrl+T/Ctrl+R/Alt+C kısayolları için kabuk entegrasyonu gerekir. | B | `download_archive` |
| [fzy](https://github.com/jhawthorn/fzy) | Hızlı bulanık bulucu. | A | `pacman` |
| [gdu](https://github.com/dundee/gdu) | Hızlı disk kullanım analizcisi (ncdu benzeri). | A | `brew` |
| [goful](https://github.com/anmitsu/goful) | Go ile yazılmış TUI dosya yöneticisi. | D | `manual` |
| [gtrash](https://github.com/umlx5h/gtrash) | rm alternatifli özellikli çöp kutusu CLI yöneticisi. | A | `brew` |
| [hunter](https://github.com/rabite0/hunter) | Rust ile yazılmış hızlı dosya yöneticisi. | C | `cargo` |
| [igrep](https://github.com/konradsz/igrep) | Etkileşimli grep / arama TUI'si. | A | `pacman` |
| [jless](https://github.com/PaulJuliusMartinez/jless) | JSON için etkileşimli komut satırı sayfalayıcı. | A | `pacman` |
| [joshuto](https://github.com/kamiyaa/joshuto) | Ranger esinli Rust terminal dosya yöneticisi. | A | `brew` |
| [lf](https://github.com/gokcehan/lf) | Go ile yazılmış terminal dosya yöneticisi. | A | `brew` |
| [lfrun](https://github.com/cirala/lfimg) | lf için görüntü önizleme sarmalayıcısı. | D | `manual` |
| [lsd](https://github.com/lsd-rs/lsd) | Renkli ikonlu modern ls alternatifi. | A | `pacman` |
| [Midnight Commander](https://midnight-commander.org/) | Klasik iki panelli terminal dosya yöneticisi. | A | `apt` |
| [ncdu](https://dev.yorhel.nl/ncdu) | ncurses disk kullanım analizcisi. | A | `apt` |
| [nnn](https://github.com/jarun/nnn) | Hafif ve hızlı terminal dosya yöneticisi. | A | `apt` |
| [ouch](https://github.com/ouch-org/ouch) | Arşiv sıkıştırma / açma için kullanıcı dostu CLI. | A | `pacman` |
| [peco](https://github.com/peco/peco) | Etkileşimli süzgeç aracı. | A | `pacman` |
| [ranger](https://github.com/ranger/ranger) | Vim tuşlarıyla çalışan Python dosya yöneticisi. | A | `apt` |
| [rclone](https://rclone.org/) | Bulut depolama için rsync benzeri senkronizasyon. | A | `pacman` |
| [rdfind](https://github.com/pauldreik/rdfind) | Yedek/yinelenen dosya bulucu. | A | `pacman` |
| [repgrep](https://github.com/acheronfail/repgrep) | ripgrep için etkileşimli bul-ve-değiştir aracı. | A | `pacman` |
| [ripgrep (rg)](https://github.com/BurntSushi/ripgrep) | Çok hızlı dosya içeriği arama aracı. | B | `download_archive` |
| [rmlint](https://github.com/sahib/rmlint) | Yinelenen dosya bulucu ve temizleyici. | A | `pacman` |
| [skim](https://github.com/skim-rs/skim) | Rust bulanık bulucu (fzf alternatifi). | A | `pacman` |
| [stu](https://github.com/lusingander/stu) | Amazon S3 tarayıcı TUI'si. | A | `brew` |
| [superfile](https://github.com/yorukot/superfile) | Modern ve güzel terminal dosya yöneticisi. | A | `brew` |
| [television](https://github.com/alexpasmantier/television) | Genel amaçlı, hızlı terminal bulanık (fuzzy) bulucu. | A | `pacman` |
| [termscp](https://github.com/veeso/termscp) | SCP/SFTP/FTP/S3/SMB için özellik zengin terminal dosya transfer TUI'si. | A | `pacman` |
| [Vifm](https://vifm.info/) | vim benzeri dosya yöneticisi. | A | `pacman` |
| [xplr](https://github.com/sayanarijit/xplr) | Hacklenebilir, minimal dosya gezgini. | A | `pacman` |
| [yazi](https://github.com/sxyazi/yazi) | Rust ile yazılmış hızlı terminal dosya yöneticisi. | C | `cargo` |

<a id="development"></a>

### Geliştirme

HTTP clients, JSON tools, language CLIs, and developer utilities.

| App | Description | Trust | Install |
|-----|-------------|:-----:|---------|
| [act](https://github.com/nektos/act) | GitHub Actions iş akışlarını yerelde çalıştırır. | A | `brew` |
| [actionlint](https://github.com/rhysd/actionlint) | GitHub Actions workflow dosyaları için statik denetleyici. | A | `pacman` |
| [ast-grep](https://ast-grep.github.io/) | AST tabanlı yapısal kod arama, lint ve yeniden yazma (sg). | A | `pacman` |
| [ATAC](https://github.com/Julien-cpsn/ATAC) | Hesapsız, çevrimdışı TUI API istemcisi (Postman alternatifi). | C | `cargo` |
| [bazel](https://bazel.build/) | Google Bazel derleme aracı. | A | `pacman` |
| [bench](https://github.com/gabriel439/bench) | Haskell benchmark aracı. | A | `pacman` |
| [black](https://github.com/psf/black) | Kararsız Python biçimlendirici. | A | `pacman` |
| [ccache](https://ccache.dev/) | Derleyici önbelleği. | A | `pacman` |
| [cgdb](https://github.com/cgdb/cgdb) | GNU Debugger için curses tabanlı TUI ön yüz. | A | `pacman` |
| [clangd](https://clangd.llvm.org/) | C/C++ dil sunucusu. | A | `pacman` |
| [cloc](https://github.com/AlDanial/cloc) | Kod satırı sayacı. | A | `pacman` |
| [cmake](https://cmake.org/) | Çapraz platform derleme sistemi. | A | `pacman` |
| [cscope](https://cscope.sourceforge.net/) | C kaynak kodu tarayıcı ve çapraz referans aracı. | A | `pacman` |
| [desed](https://github.com/SoptikHa2/desed) | sed betikleri için etkileşimli hata ayıklama TUI'si. | A | `brew` |
| [direnv](https://direnv.net/) | Dizine özel ortam değişkenlerini otomatik yükler. | A | `apt` |
| [ec](https://github.com/editorconfig-checker/editorconfig-checker) | EditorConfig doğrulayıcı. | A | `pacman` |
| [eslint](https://eslint.org/) | JavaScript/TypeScript linter. | C | `npm` |
| [euporie](https://github.com/joouha/euporie) | Terminalde Jupyter notebook istemcisi. | C | `pipx` |
| [flamegraph](https://github.com/brendangregg/FlameGraph) | Flame graph betikleri. | A | `pacman` |
| [fx](https://github.com/antonmedv/fx) | Etkileşimli terminal JSON görüntüleyici ve işleyici. | C | `npm` |
| [gdb](https://www.gnu.org/software/gdb/) | GNU hata ayıklayıcı. | A | `pacman` |
| [gopls](https://github.com/golang/tools) | Go dil sunucusu. | A | `pacman` |
| [heaptrack](https://github.com/KDE/heaptrack) | Yığın bellek profilleyicisi. | A | `pacman` |
| [HTTPie](https://httpie.io/) | İnsan dostu HTTP istemcisi. | A | `apt` |
| [hyperfine](https://github.com/sharkdp/hyperfine) | Komut satırı kıyaslama aracı. | A | `apt` |
| [jqp](https://github.com/noahgorstein/jqp) | jq ifadelerini denemek için TUI oyun alanı. | A | `brew` |
| [just](https://github.com/casey/just) | Komut çalıştırıcı; Makefile'a modern alternatif. | A | `apt` |
| [kaskade](https://github.com/sauljabin/kaskade) | Apache Kafka için metin kullanıcı arayüzü. | A | `brew` |
| [lldb](https://lldb.llvm.org/) | LLVM hata ayıklayıcı. | A | `pacman` |
| [loc](https://github.com/cgag/loc) | Hızlı satır sayacı (Rust). | C | `cargo` |
| [ltrace](https://www.ltrace.org/) | Kütüphane çağrısı izleyici. | A | `pacman` |
| [meson](https://mesonbuild.com/) | Hızlı ve kullanıcı dostu derleme sistemi. | A | `pacman` |
| [mise](https://mise.jdx.dev/) | Çoklu dil sürüm yöneticisi (asdf alternatifi). | A | `brew` |
| [mitmproxy](https://www.mitmproxy.org) | Etkileşimli HTTPS ara sunucusu ve trafik inceleme aracı. | A | `apt` |
| [mold](https://github.com/rui314/mold) | Modern hızlı bağlayıcı (linker). | A | `pacman` |
| [mypy](https://mypy-lang.org/) | Python statik tür denetleyici. | A | `pacman` |
| [nap](https://github.com/maaslalani/nap) | Terminal kod parçacığı (snippet) yöneticisi. | A | `brew` |
| [ninja](https://ninja-build.org/) | Küçük ve hızlı derleme sistemi. | A | `pacman` |
| [openapi-tui](https://github.com/zaghaghi/openapi-tui) | OpenAPI tanımlarını listeleyip tarayan ve çalıştıran TUI. | A | `pacman` |
| [perf](https://perf.wiki.kernel.org/) | Linux performans sayaçları. | A | `pacman` |
| [posting](https://github.com/darrenburns/posting) | Terminalde yaşayan güçlü HTTP istemcisi. | C | `pipx` |
| [pre-commit](https://pre-commit.com/) | Git kanca yöneticisi. | A | `pacman` |
| [presenterm](https://github.com/mfontanini/presenterm) | Markdown sunumlarını terminalde gösteren araç. | A | `pacman` |
| [prettier](https://prettier.io/) | Kod biçimlendirici. | C | `npm` |
| [pudb](https://github.com/inducer/pudb) | Tam ekran konsol tabanlı Python hata ayıklayıcı. | A | `pacman` |
| [pyright](https://github.com/microsoft/pyright) | Microsoft Python dil sunucusu CLI. | C | `npm` |
| [resterm](https://github.com/unkn0wn-root/resterm) | HTTP, GraphQL, gRPC ve WebSocket için terminal API istemcisi. | A | `brew` |
| [ruff](https://github.com/astral-sh/ruff) | Çok hızlı Python linter ve biçimlendirici. | C | `pipx` |
| [runme](https://github.com/stateful/runme) | Markdown runbook ve README içindeki komutları çalıştırır. | A | `brew` |
| [rust-analyzer](https://rust-analyzer.github.io/) | Rust dil sunucusu. | A | `pacman` |
| [scc](https://github.com/boyter/scc) | Hızlı kod satırı / karmaşıklık sayacı (Sloc Cloc and Code). | A | `brew` |
| [sccache](https://github.com/mozilla/sccache) | Paylaşımlı derleme önbelleği (Rust/C++). | A | `pacman` |
| [scooter](https://github.com/thomasschafer/scooter) | Etkileşimli bul ve değiştir TUI'si. | A | `brew` |
| [sequin](https://github.com/charmbracelet/sequin) | ANSI kaçış dizilerini okunabilir gösteren Charm aracı. | A | `brew` |
| [ShellCheck](https://www.shellcheck.net/) | Kabuk betiği statik analiz aracı. | A | `apt` |
| [shfmt](https://github.com/mvdan/sh) | Kabuk betik biçimlendirici. | A | `pacman` |
| [slumber](https://github.com/LucasPickering/slumber) | Terminal tabanlı REST / HTTP istemcisi. | A | `pacman` |
| [strace](https://strace.io/) | Sistem çağrısı izleyici. | A | `pacman` |
| [tftui](https://github.com/idoavrah/terraform-tui) | Terraform plan/state için metin kullanıcı arayüzü. | C | `pipx` |
| [tokei](https://github.com/XAMPPRocky/tokei) | Kod satırı ve dil istatistikleri sayacı. | C | `cargo` |
| [tsc](https://www.typescriptlang.org/) | TypeScript derleyicisi. | A | `pacman` |
| [uv](https://github.com/astral-sh/uv) | Astral'ın çok hızlı Python paket ve proje yöneticisi. | A | `brew` |
| [valgrind](https://valgrind.org/) | Bellek hata dedektörü. | A | `pacman` |
| [watchexec](https://github.com/watchexec/watchexec) | Dosya değişikliklerinde komut çalıştıran izleyici. | C | `cargo` |
| [xh](https://github.com/ducaale/xh) | Rust ile yazılmış hızlı HTTPie dostu HTTP istemcisi. | C | `cargo` |
| [yapf](https://github.com/google/yapf) | Python biçimlendirici. | C | `pipx` |
| [yozefu](https://github.com/MAIF/yozefu) | Kafka kümelerindeki veriyi keşfetmek için TUI. | A | `brew` |

<a id="editors"></a>

### Editörler

Terminal editors and modal text editing tools.

| App | Description | Trust | Install |
|-----|-------------|:-----:|---------|
| [amp](https://github.com/jmacdonald/amp) | Tam özellikli terminal metin editörü. | C | `cargo` |
| [dhex](https://www.dettus.net/dhex/) | Ncurses hex editörü. | A | `pacman` |
| [durdraw](https://github.com/cmang/durdraw) | ASCII/ANSI sanat çizimi için çok yönlü metin düzenleyici. | A | `brew` |
| [edi](https://www.enlightenment.org/) | Enlightenment tabanlı metin editörü (CLI odak). | A | `pacman` |
| [Emacs](https://www.gnu.org/software/emacs/) | Genişletilebilir metin editörü ve uygulama ortamı. | A | `apt` |
| [Frogmouth](https://github.com/Textualize/frogmouth) | Terminal Markdown tarayıcı/okuyucu. | C | `pipx` |
| [Helix](https://helix-editor.com/) | Modal, seçim-öncelikli modern terminal editörü. | C | `cargo` |
| [hexedit](https://github.com/pixel/hexedit) | Basit hex/binary editörü. | A | `pacman` |
| [HTE](https://hte.sourceforge.net/) | Hex / metin editörü (hte). | A | `pacman` |
| [joe](https://joe-editor.sourceforge.io/) | Joe's Own Editor — kolay öğrenilir. | A | `pacman` |
| [Kakoune](https://kakoune.org/) | Seçim-öncelikli modal kod editörü. | A | `apt` |
| [md-tui](https://github.com/henriklovhaug/md-tui) | Terminalde Markdown işleyici / görüntüleyici. | A | `pacman` |
| [micro](https://micro-editor.github.io/) | Sezgisel, modern terminal metin editörü. | A | `apt` |
| [Microsoft Edit](https://github.com/microsoft/edit) | Microsoft Edit (msedit) basit terminal metin düzenleyicisi. | A | `pacman` |
| [nano](https://www.nano-editor.org/) | Basit ve yaygın terminal editörü. | A | `pacman` |
| [ne](https://ne.di.unimi.it/) | Nice Editor — kullanıcı dostu metin editörü. | A | `pacman` |
| [Neovim](https://neovim.io/) | Vim'in genişletilebilir modern çatalı. | A | `apt` |
| [orbiton](https://github.com/xyproto/orbiton) | Yapılandırılabilir terminal editörü (o). | A | `pacman` |
| [tilde](https://os.ghalkes.nl/tilde/) | Sezgisel terminal metin editörü. | A | `pacman` |
| [treemd](https://github.com/Epistates/treemd) | Ağaç tabanlı yapısal Markdown gezgini. | A | `pacman` |
| [Vim](https://www.vim.org/) | Klasik gelişmiş metin editörü. | A | `apt` |
| [vis](https://github.com/martanne/vis) | vi benzeri yapılandırılabilir editör. | A | `pacman` |

<a id="system"></a>

### Sistem

Process monitors, disk tools, and host observability.

| App | Description | Trust | Install |
|-----|-------------|:-----:|---------|
| [acpi](https://sourceforge.net/projects/acpiclient/) | Pil/ACPI bilgi aracı. | A | `pacman` |
| [alsamixer](https://www.alsa-project.org/) | ALSA ses karıştırıcı. | A | `pacman` |
| [bottom](https://github.com/ClementTsang/bottom) | Özelleştirilebilir grafik süreç/sistem monitörü (btm). | C | `cargo` |
| [brightnessctl](https://github.com/Hummer12007/brightnessctl) | Ekran parlaklığı kontrolü. | A | `pacman` |
| [btop](https://github.com/aristocratos/btop) | CPU, bellek, disk ve ağ kullanımını grafik olarak izler. | A | `apt` |
| [caligula](https://github.com/ifd3f/caligula) | Kullanıcı dostu hafif disk kalıbı yazma TUI'si. | A | `pacman` |
| [duf](https://github.com/muesli/duf) | Diskleri ve doluluk oranlarını tablo hâlinde gösterir. | B | `download_archive` |
| [fastfetch](https://github.com/fastfetch-cli/fastfetch) | Hızlı sistem bilgisi / neofetch tarzı özet. | A | `apt` |
| [Glances](https://github.com/nicolargo/glances) | Çok panelli sistem izleyici; top/htop alternatifi. | A | `apt` |
| [htop](https://htop.dev/) | Etkileşimli süreç izleyici; top alternatifi. | A | `apt` |
| [inxi](https://smxi.org/docs/inxi.htm) | Sistem bilgi özeti. | A | `pacman` |
| [kmon](https://github.com/orhun/kmon) | Linux çekirdek yöneticisi ve etkinlik monitörü. | C | `cargo` |
| [lazyjournal](https://github.com/Lifailon/lazyjournal) | journalctl, dosya ve konteyner günlükleri için TUI. | A | `brew` |
| [mac-cleanup-go](https://github.com/2ykwang/mac-cleanup-go) | [macOS] Önbellek/log tarayıp Trash’e taşıyan disk temizleme TUI’si. | A | `brew` |
| [macchina](https://github.com/Macchina-CLI/macchina) | Hızlı sistem bilgisi (Rust). | A | `pacman` |
| [macmon](https://github.com/vladkens/macmon) | [macOS] Apple Silicon için sudosuz gerçek zamanlı performans monitörü. | A | `brew` |
| [ncpamixer](https://github.com/fulhax/ncpamixer) | ncurses PulseAudio karıştırıcı. | A | `pacman` |
| [neofetch](https://github.com/dylanaraps/neofetch) | Sistem bilgisi ASCII logo ile (bakımda). | A | `pacman` |
| [nerdlog](https://github.com/dimonomid/nerdlog) | Zaman çizelgeli, uzak öncelikli çoklu host TUI log görüntüleyici. | A | `brew` |
| [nmon](https://nmon.sourceforge.io/) | Linux performans ve kaynak izleme aracı. | A | `pacman` |
| [nvtop](https://github.com/Syllo/nvtop) | AMD, Intel ve NVIDIA GPU süreç monitörü. | A | `apt` |
| [paleofetch](https://github.com/ssleert/paleofetch) | C ile yazılmış hızlı neofetch. | D | `manual` |
| [powertop](https://github.com/fenrus75/powertop) | Güç tüketimi analizcisi. | A | `pacman` |
| [procs](https://github.com/dalance/procs) | Modern, kullanıcı dostu ps alternatifi. | C | `cargo` |
| [pstop](https://github.com/psmux/pstop) | [Windows] Çekirdek başına CPU çubukları ve ağaç görünümlü htop tarzı sistem monitörü. | C | `cargo` |
| [pulsemixer](https://github.com/GeorgeFilipkin/pulsemixer) | PulseAudio/PipeWire TUI karıştırıcı. | A | `pacman` |
| [screenfetch](https://github.com/KittyKatt/screenFetch) | Sistem bilgisi görüntüleyici. | A | `pacman` |
| [sensors](https://hwmon.wiki.kernel.org/lm_sensors) | Donanım sensörleri. | A | `pacman` |
| [sysdig](https://github.com/draios/sysdig) | Sistem ve konteyner keşif / sorun giderme aracı (csysdig TUI). | A | `pacman` |
| [systemctl-tui](https://github.com/rgwood/systemctl-tui) | systemctl-tui, systemd birimlerini ve günlüklerini yönetmek için hızlı ve sade bir TUI’dir: servis/zamanlayıcı durumu ve logları gezme, başlat/durdur, birim dosyası görüntüleme/düzenleme. --host user@host ile SSH üzerinden uzaktan yönetim (uzakta ek kurulum gerekmez). Nova servis yöneticisi değildir; systemctl-tui Lazygit tarzı bir systemd yüzeyidir. | A | `pacman` |
| [sysz](https://github.com/joehillen/sysz) | systemctl için fzf tabanlı TUI. | D | `manual` |
| [zenith](https://github.com/bvaisvil/zenith) | Grafik metriklerle terminal sistem monitörü. | C | `cargo` |

<a id="panels"></a>

### Paneller

Dashboards and system overview panels.

| App | Description | Trust | Install |
|-----|-------------|:-----:|---------|
| [atop](https://www.atoptool.nl/) | Gelişmiş sistem/process izleyici. | A | `pacman` |
| [bashtop](https://github.com/aristocratos/bashtop) | Bash kaynak izleyici (btop atası). | A | `pacman` |
| [below](https://github.com/facebookincubator/below) | Facebook'un zaman yolculuklu kaynak izleyicisi. | A | `pacman` |
| [bmon](https://github.com/tgraf/bmon) | Bant genişliği izleyici ve hız ölçer. | A | `pacman` |
| [bpytop](https://github.com/aristocratos/bpytop) | Python kaynak izleyici. | A | `pacman` |
| [cointop](https://github.com/cointop-sh/cointop) | Kripto para takip TUI. | A | `pacman` |
| [GoAccess](https://goaccess.io/) | Gerçek zamanlı web günlük analizcisi. | A | `pacman` |
| [gonzo](https://github.com/control-theory/gonzo) | k9s esinli gerçek zamanlı log analiz TUI'si. | A | `brew` |
| [gotop](https://github.com/xxxserxxx/gotop) | Grafiksel sistem izleyici. | A | `pacman` |
| [hwatch](https://github.com/black-desk/hwatch) | Modern watch alternatifi (geçmiş/diff). | C | `cargo` |
| [iftop](https://www.ex-parrot.com/pdw/iftop/) | Ağ bant genişliği izleyici. | A | `pacman` |
| [iotop](https://github.com/Tomas-M/iotop) | I/O kullanım izleyici. | A | `pacman` |
| [nethogs](https://github.com/raboof/nethogs) | Süreç bazlı ağ kullanımı. | A | `pacman` |
| [otel-tui](https://github.com/ymtdzzz/otel-tui) | OpenTelemetry verisi için terminal görüntüleyici. | A | `brew` |
| [Planor](https://github.com/mrusme/planor) | Bulut kaynak panosu (AWS vb.). | D | `manual` |
| [process-compose](https://github.com/f1bonacc1/process-compose) | Süreç orkestrasyon TUI (docker-compose benzeri). | D | `manual` |
| [s-tui](https://github.com/amanusk/s-tui) | CPU sıcaklık/gerilim stres terminal UI. | C | `pipx` |
| [ticker](https://github.com/achannarasappa/ticker) | Hisse senedi, kripto ve türev fiyatlarını terminalde izler. | A | `brew` |
| [tiptop](https://github.com/nschloe/tiptop) | Modern kaynak izleyici. | C | `pipx` |
| [viddy](https://github.com/sachaos/viddy) | Modern watch, tarihçe ve diff ile. | A | `pacman` |
| [ytop](https://github.com/cjbassi/ytop) | Rust TUI sistem izleyici (gotop esinli). | C | `cargo` |

<a id="networking"></a>

### Ağ

DNS, bandwidth, traceroute, and network diagnostics.

| App | Description | Trust | Install |
|-----|-------------|:-----:|---------|
| [AdGuardian](https://github.com/lissy93/AdGuardian-Term) | AdGuard Home için gerçek zamanlı trafik izleme TUI (resmi olmayan). | C | `cargo` |
| [aria2](https://aria2.github.io/) | Çok protokolü destekleyen indirme yardımcısı. | A | `apt` |
| [bandwhich](https://github.com/imsnif/bandwhich) | Ağ bant genişliğini süreç ve bağlantı bazında gösterir. Yerel arayüzleri izlemek için ek izinler gerekebilir. | C | `cargo` |
| [croc](https://github.com/schollz/croc) | Bilgisayarlar arası kolay ve güvenli dosya transferi. | A | `pacman` |
| [curl](https://curl.se/) | Veri transfer ve HTTP istek aracı. | A | `apt` |
| [curlie](https://github.com/rs/curlie) | curl gücü, HTTPie kullanım kolaylığı. | A | `pacman` |
| [dig](https://www.isc.org/bind/) | DNS sorgu aracı (bind). | A | `pacman` |
| [dog](https://github.com/ogham/dog) | Kullanıcı dostu DNS istemcisi; dig alternatifi. | C | `cargo` |
| [doggo](https://github.com/mr-karan/doggo) | İnsan dostu komut satırı DNS istemcisi. | A | `pacman` |
| [gping](https://github.com/orf/gping) | Grafikli ping; birden fazla hostu görsel izler. | C | `cargo` |
| [iperf3](https://iperf.fr/) | Ağ performans ölçümü. | A | `pacman` |
| [mosh](https://mosh.org/) | Kopmalara dayanıklı mobil kabuk (SSH alternatifi). | A | `pacman` |
| [mtr](https://github.com/traviscross/mtr) | ping ve traceroute'u birleştiren ağ tanılama aracı. Hedef adresi vermek gerekir. | A | `apt` |
| [ncat](https://nmap.org/ncat/) | Nmap netcat (ncat). | A | `pacman` |
| [netcat](https://nmap.org/ncat/) | TCP/UDP İsviçre çakısı. | A | `pacman` |
| [nmap](https://nmap.org/) | Ağ keşif ve güvenlik tarama aracı. | A | `apt` |
| [oha](https://github.com/hatoo/oha) | HTTP yük üreteci (rakyll/hey esinli, TUI). | A | `pacman` |
| [oryx](https://github.com/pythops/oryx) | eBPF ile ağ trafiği dinleme TUI'si. | A | `pacman` |
| [psnet](https://github.com/psmux/psnet) | [Windows] Hız grafikleri ve DNS çözümlemeli gerçek zamanlı ağ monitörü TUI. | C | `cargo` |
| [rustnet](https://github.com/domcyrus/rustnet) | eBPF ve paket incelemesiyle gerçek zamanlı ağ izleme TUI'si. | A | `pacman` |
| [rustscan](https://github.com/bee-san/RustScan) | Hızlı modern port tarayıcı. | A | `pacman` |
| [socat](https://github.com/3ndG4me/socat) | Çok amaçlı röle (netcat++). | A | `pacman` |
| [speedtest-cli](https://github.com/sivel/speedtest-cli) | Ookla hız testi CLI. | A | `pacman` |
| [Tailscale](https://tailscale.com/) | Tailscale, WireGuard® tabanlı özel ağları kolaylaştıran açık kaynak istemcidir: tailscaled arka plan hizmeti ve tailscale CLI ile cihazları tailnet’e bağlar, durum ve IP tanılaması yapar. Paketler pkgs.tailscale.com üzerinden sunulur. Nova bir VPN değildir; Tailscale makinenizi kimlik doğrulamalı şifreli mesh ağına ekler (elevated kurulum gerekir). | A | `pacman` |
| [tcpdump](https://www.tcpdump.org/) | Paket yakalama. | A | `pacman` |
| [termshark](https://github.com/gcla/termshark) | Wireshark/tshark için terminal arayüzü. | A | `brew` |
| [trippy](https://github.com/fujiapple852/trippy) | mtr benzeri modern ağ tanılama aracı (trip). | C | `cargo` |
| [updo](https://github.com/Owloops/updo) | Uyarı destekli uptime izleme CLI aracı. | A | `brew` |
| [wget](https://www.gnu.org/software/wget/) | Dosya indirme aracı. | A | `apt` |
| [whois](https://github.com/rfc1036/whois) | WHOIS sorgu aracı. | A | `pacman` |
| [WireGuard tools](https://www.wireguard.com/) | wireguard-tools, modern VPN tüneli WireGuard için kullanıcı alanı araçlarını sağlar: wg ile anahtar üretimi ve arayüz yapılandırması, wg-quick ile hızlı up/down. Kernel veya wireguard-go üzerinden çalışır; SSH benzeri genel anahtar değişimiyle kurulur, IPsec/OpenVPN’e göre daha sade ve performanslıdır. Nova ağ tüneli kurmaz; bu paket WireGuard arayüzlerini yönetir (root/CAP_NET_ADMIN). | A | `pacman` |
| [wishlist](https://github.com/charmbracelet/wishlist) | Birden fazla SSH ucu için tek giriş noktası (Charm). | A | `pacman` |

<a id="containers"></a>

### Konteyner

Docker, Kubernetes, and container inspection tools.

| App | Description | Trust | Install |
|-----|-------------|:-----:|---------|
| [buildah](https://buildah.io/) | OCI imaj oluşturma aracı. | A | `pacman` |
| [cdebug](https://github.com/iximiuz/cdebug) | Çalışan konteynerlere debug kabuğu. | D | `manual` |
| [ctop](https://github.com/bcicen/ctop) | Konteynerler için top benzeri metrik arayüzü. | A | `brew` |
| [distrobox](https://github.com/89luca89/distrobox) | Herhangi bir Linux dağıtımını terminalde kullanmayı sağlar. | A | `pacman` |
| [dive](https://github.com/wagoodman/dive) | Konteyner imaj katmanlarını keşfeder. | A | `brew` |
| [docker](https://www.docker.com/) | Docker Engine CLI istemcisi. | A | `pacman` |
| [docker-compose](https://docs.docker.com/compose/) | Docker Compose V2 eklentisi (compose). | A | `pacman` |
| [dockly](https://github.com/lirantal/dockly) | Docker konteyner ve servis yönetimi için immersive TUI. | A | `brew` |
| [dry](https://github.com/moncho/dry) | Docker ve Docker Swarm için terminal yöneticisi. | D | `manual` |
| [dtop](https://github.com/amir20/dtop) | Birden fazla host üzerinde Docker izleme terminal panosu. | A | `brew` |
| [ducker](https://github.com/robertpsoane/ducker) | k9s tarzı Docker yönetim TUI'si. | A | `pacman` |
| [e1s](https://github.com/keidarcy/e1s) | AWS ECS yönetimi için k9s esinli TUI. | A | `brew` |
| [hadolint](https://github.com/hadolint/hadolint) | Dockerfile linter. | A | `pacman` |
| [Helm](https://helm.sh/) | Kubernetes paket yöneticisi. | A | `brew` |
| [helmfile](https://github.com/helmfile/helmfile) | Helm release bildirimsel dağıtım. | A | `pacman` |
| [k9s](https://k9scli.io/) | Kubernetes kümelerini yönetmek için terminal panosu. | A | `brew` |
| [kdash](https://github.com/kdash-rs/kdash) | Kubernetes için basit ve hızlı pano. | C | `cargo` |
| [kind](https://kind.sigs.k8s.io/) | Docker içinde yerel Kubernetes kümeleri. | A | `pacman` |
| [ktop](https://github.com/vladimirvivien/ktop) | Kubernetes için top benzeri izleyici. | D | `manual` |
| [kubectl](https://kubernetes.io/docs/reference/kubectl/) | Kubernetes komut satırı aracı. | A | `brew` |
| [kubectx](https://github.com/ahmetb/kubectx) | Kubernetes context/namespace değiştirici. | A | `pacman` |
| [kubens](https://github.com/ahmetb/kubectx) | Kubernetes namespace değiştirici. | A | `pacman` |
| [kubetui](https://github.com/sarub0b0/kubetui) | Kubernetes kaynakları için TUI. | C | `cargo` |
| [kustomize](https://kustomize.io/) | Kubernetes YAML özelleştirme. | A | `pacman` |
| [lazycontainer](https://github.com/andreybleme/lazycontainer) | [macOS] Apple Containers yönetimi için TUI. | A | `brew` |
| [lazydocker](https://github.com/jesseduffield/lazydocker) | Docker konteynerleri, imajları ve günlükleri için terminal arayüzü. | B | `download_archive` |
| [lfk](https://github.com/janosmiko/lfk) | Kubernetes kaynaklarını gezmek için klavye odaklı TUI. | A | `brew` |
| [minikube](https://minikube.sigs.k8s.io/) | Yerel Kubernetes kümesi. | A | `pacman` |
| [nerdctl](https://github.com/containerd/nerdctl) | containerd için Docker uyumlu CLI. | A | `pacman` |
| [Oxker](https://github.com/mrjackwills/oxker) | Docker konteyner yönetimi için hafif TUI. | C | `cargo` |
| [podman](https://podman.io/) | Kök gerektirmeyen konteyner motoru. | A | `pacman` |
| [podman-tui](https://github.com/containers/podman-tui) | Podman için resmi terminal kullanıcı arayüzü. | A | `brew` |
| [regctl](https://github.com/regclient/regclient) | Konteyner kayıt defteri CLI. | D | `manual` |
| [sen](https://github.com/TomasTomecek/sen) | Docker engine için terminal kullanıcı arayüzü. | C | `pipx` |
| [skopeo](https://github.com/containers/skopeo) | Konteyner imajı inceleme/taşıma. | A | `pacman` |
| [stern](https://github.com/stern/stern) | Çoklu pod log kuyruğu. | A | `pacman` |
| [wander](https://github.com/robinovitch61/wander) | HashiCorp Nomad için terminal TUI. | A | `brew` |

<a id="database"></a>

### Veritabanı

Database CLIs, TUI clients, and query helpers.

| App | Description | Trust | Install |
|-----|-------------|:-----:|---------|
| [chdig](https://github.com/azat/chdig) | ClickHouse için TUI keşif aracı. | A | `brew` |
| [datasette](https://datasette.io/) | SQLite’ı web/API olarak yayınla. | C | `pipx` |
| [dblab](https://github.com/danvergara/dblab) | Komut satırı meraklıları için veritabanı istemcisi TUI. | A | `brew` |
| [dolphie](https://github.com/charles-001/dolphie) | MySQL/MariaDB için gerçek zamanlı analitik TUI. | A | `brew` |
| [gobang](https://github.com/TaKO8Ki/gobang) | Çok platformlu TUI veritabanı yönetim aracı. | C | `cargo` |
| [Harlequin](https://github.com/tconbeer/harlequin) | Terminal için SQL IDE. | C | `pipx` |
| [iredis](https://github.com/laixintao/iredis) | Otomatik tamamlamalı Redis terminal istemcisi. | C | `pipx` |
| [lazysql](https://github.com/jorgerojas26/lazysql) | Veritabanlarını gezmek için terminal arayüzü. | D | `manual` |
| [litecli](https://litecli.com/) | SQLite için otomatik tamamlamalı CLI. | C | `pipx` |
| [mongosh](https://www.mongodb.com/docs/mongodb-shell/) | MongoDB kabuğu. | A | `pacman` |
| [mycli](https://github.com/dbcli/mycli) | Otomatik tamamlama özellikli MySQL/MariaDB istemcisi. | C | `pipx` |
| [pg_activity](https://github.com/dalibo/pg_activity) | PostgreSQL sunucu etkinliğini izleyen etkileşimli terminal aracı (Dalibo). Çalışan, bekleyen ve bloke eden sorguları canlı listeler; CPU/bellek/IO, TPS, kilitler ve geçici dosya boyutunu gösterir. Sorguları iptal veya sonlandırabilir; CSV çıktısı, profiller (narrow/wide/minimal) ve AWS RDS seçenekleri vardır. Yerel veya uzak bağlantı; tam sistem bilgisi için postgres kullanıcısı önerilir. | C | `pipx` |
| [pgcli](https://github.com/dbcli/pgcli) | Otomatik tamamlama özellikli PostgreSQL istemcisi. | C | `pipx` |
| [psql](https://www.postgresql.org/) | PostgreSQL etkileşimli terminal. | A | `pacman` |
| [rainfrog](https://github.com/achristmascarl/rainfrog) | Postgres, MySQL ve SQLite için veritabanı TUI. | C | `cargo` |
| [redis-cli](https://redis.io/) | Redis CLI. | A | `pacman` |
| [sqlite-utils](https://sqlite-utils.datasette.io/) | SQLite CLI yardımcıları. | C | `pipx` |
| [sqlite3](https://www.sqlite.org/) | SQLite komut satırı kabuğu. | A | `apt` |
| [usql](https://github.com/xo/usql) | Çoklu veritabanı için evrensel SQL CLI. | A | `brew` |

<a id="security"></a>

### Güvenlik

Crypto, secrets, scanners, and signing tooling.

| App | Description | Trust | Install |
|-----|-------------|:-----:|---------|
| [age](https://github.com/FiloSottile/age) | Basit, modern ve güvenli dosya şifreleme aracı. | A | `apt` |
| [binsider](https://github.com/orhun/binsider) | Linux ikili dosyalarını analiz eden TUI. | C | `cargo` |
| [cosign](https://github.com/sigstore/cosign) | Sigstore ile konteyner ve artefakt imzalama / doğrulama. | A | `pacman` |
| [cotp](https://github.com/replydev/cotp) | Şifreli komut satırı TOTP/HOTP kimlik doğrulayıcı. | A | `pacman` |
| [gitleaks](https://github.com/gitleaks/gitleaks) | Git depolarında sızdırılmış sır ve anahtar tarayıcısı. | A | `pacman` |
| [gopass](https://github.com/gopasspw/gopass) | Ekipler için Unix parola yöneticisi (pass uyumlu). | A | `pacman` |
| [gpg-tui](https://github.com/orhun/gpg-tui) | GnuPG için terminal kullanıcı arayüzü. | C | `cargo` |
| [grype](https://github.com/anchore/grype) | Konteyner imajı ve dosya sistemi güvenlik açığı tarayıcısı (Anchore). | A | `pacman` |
| [hashcat](https://hashcat.net/hashcat/) | Gelişmiş parola kurtarma. | A | `pacman` |
| [hydra](https://github.com/vanhauser-thc/thc-hydra) | Ağ oturum açma denetleyici. | A | `pacman` |
| [John the Ripper](https://www.openwall.com/john/) | Parola kırma aracı. | A | `pacman` |
| [masscan](https://github.com/robertdavidgraham/masscan) | Çok hızlı port tarayıcı. | A | `pacman` |
| [nikto](https://github.com/sullo/nikto) | Web sunucu tarayıcı. | A | `pacman` |
| [Nuclei](https://github.com/projectdiscovery/nuclei) | ProjectDiscovery’nin YAML şablonlarıyla çalışan yüksek performanslı güvenlik açığı tarayıcısı. Topluluk şablonlarıyla gerçekçi adımlarla doğrulama yaparak yanlış pozitifleri azaltmayı hedefler; TCP/DNS/HTTP/SSL ve daha fazla protokol, paralel tarama ve CI/CD entegrasyonu destekler. Nova tarayıcı değildir; Nuclei hedeflerde şablon tabanlı güvenlik taraması çalıştırır (yalnızca yetkili sistemlerde kullanın). | B | `download_archive` |
| [osv-scanner](https://github.com/google/osv-scanner) | OSV veritabanı ile bağımlılık güvenlik açığı tarayıcısı. | A | `pacman` |
| [pass](https://www.passwordstore.org/) | Unix parola yöneticisi (the standard unix password manager). | A | `apt` |
| [prs](https://github.com/timvisee/prs) | GPG ve git senkronlu parola yöneticisi CLI. | A | `brew` |
| [rbw](https://github.com/doy/rbw) | Resmi olmayan Bitwarden komut satırı istemcisi. | A | `pacman` |
| [Semgrep](https://github.com/semgrep/semgrep) | Semgrep, kodda hata ve güvenlik sorunlarını arayan hızlı açık kaynak statik analiz (SAST) aracıdır: 30+ dil, semantik arama (grep gibi ama AST duyarlı), IDE/pre-commit/CI kullanımı. Kurallar yazdığınız koda benzer; varsayılan olarak kod yüklenmez. Community Edition dosya/fonksiyon sınırlıdır. Nova kod tarayıcısı değildir; Semgrep depoda güvenlik ve kalite kurallarını uygular. | C | `pipx` |
| [sops](https://github.com/getsops/sops) | Mozilla/CNCF sırları şifreleme aracı (YAML/JSON/ENV). | A | `brew` |
| [sqlmap](https://sqlmap.org/) | SQL enjeksiyon test aracı. | A | `pacman` |
| [syft](https://github.com/anchore/syft) | Konteyner ve dosya sistemlerinden SBOM üretici (Anchore). | A | `pacman` |
| [Trivy](https://trivy.dev/) | Konteyner, FS ve Git deposu güvenlik tarayıcısı. | A | `brew` |
| [tshark](https://www.wireshark.org/) | Wireshark CLI (tshark). | A | `pacman` |
| [Vault CLI](https://www.vaultproject.io/) | HashiCorp Vault komut satırı istemcisi. | A | `brew` |

<a id="media"></a>

### Medya

Audio, video, and image terminal tools.

| App | Description | Trust | Install |
|-----|-------------|:-----:|---------|
| [catimg](https://github.com/posva/catimg) | Görselleri 256 renkli terminalde yazdırır. | A | `pacman` |
| [cava](https://github.com/karlstav/cava) | Konsol tabanlı ses görselleştirici. | A | `apt` |
| [cmus](https://cmus.github.io/) | Hafif ncurses müzik çalar. | A | `apt` |
| [ffmpeg](https://ffmpeg.org/) | Ses/video dönüştürme ve işleme araç seti. | A | `apt` |
| [freeze](https://github.com/charmbracelet/freeze) | Kod ve terminal çıktısından görüntü üreten Charm aracı. | A | `brew` |
| [jp2a](https://github.com/cslarsen/jp2a) | JPEG görsellerini ASCII sanata dönüştürür. | A | `pacman` |
| [mpc](https://www.musicpd.org/clients/mpc/) | MPD için minimalist komut satırı istemcisi. | A | `pacman` |
| [mpsyt](https://github.com/mps-youtube/mps-youtube) | YouTube müzik CLI (bakımda). | C | `pipx` |
| [mpv](https://mpv.io/) | Özgür, açık kaynaklı medya oynatıcı (CLI/TUI dostu). | A | `apt` |
| [ncmpcpp](https://github.com/ncmpcpp/ncmpcpp) | MPD için özellikli müzik istemcisi. | A | `pacman` |
| [ncspot](https://github.com/hrkfdn/ncspot) | Spotify için ncurses istemcisi. | C | `cargo` |
| [playerctl](https://github.com/altdesktop/playerctl) | MPRIS medya oynatıcı denetleyicisi (Spotify, VLC, …). | A | `pacman` |
| [spt](https://github.com/Rigellute/spotify-tui) | Spotify TUI istemcisi. | A | `pacman` |
| [termusic](https://github.com/tramhao/termusic) | Rust terminal müzik çalar. | C | `cargo` |
| [timg](https://github.com/hzeller/timg) | Terminal görüntü ve video görüntüleyici. | A | `brew` |
| [viu](https://github.com/atanunq/viu) | Basit terminal görüntü görüntüleyici. | A | `pacman` |
| [yt-dlp](https://github.com/yt-dlp/yt-dlp) | YouTube ve diğer sitelerden video/ses indirme aracı. | A | `apt` |
| [ytfzf](https://github.com/pystardust/ytfzf) | YouTube arama/oynatma (fzf). | A | `pacman` |

<a id="messaging"></a>

### Mesajlaşma

IRC, Matrix, and chat terminal clients.

| App | Description | Trust | Install |
|-----|-------------|:-----:|---------|
| [aerc](https://aerc-mail.org/) | E-posta için zarif terminal istemcisi. | A | `apt` |
| [discordo](https://github.com/ayn2op/discordo) | Hafif Discord TUI. | A | `pacman` |
| [gomuks](https://github.com/tulir/gomuks) | Matrix için terminal istemcisi. | D | `manual` |
| [himalaya](https://github.com/pimalaya/himalaya) | E-posta için CLI; MUA ile birlikte kullanılabilir. | C | `cargo` |
| [iamb](https://github.com/ulyssa/iamb) | Vim kullanıcıları için Matrix istemcisi. | A | `brew` |
| [irssi](https://irssi.org/) | Modüler IRC istemcisi. | A | `apt` |
| [isync](https://isync.sourceforge.io/) | IMAP ve Maildir posta kutusu senkronizasyonu (mbsync). | A | `pacman` |
| [mutt](https://www.mutt.org/) | Küçük ama güçlü metin tabanlı e-posta istemcisi. | A | `pacman` |
| [NeoMutt](https://neomutt.org/) | Mutt'un gelişmiş e-posta istemcisi çatalı. | A | `apt` |
| [notmuch](https://notmuchmail.org/) | Hızlı, etiket tabanlı e-posta indeksleyici ve arayüz. | A | `pacman` |
| [offlineimap](https://github.com/OfflineIMAP/offlineimap3) | İki depo arasında e-posta senkronizasyonu. | A | `pacman` |
| [pop](https://github.com/charmbracelet/pop) | Terminalden e-posta gönderen Charm aracı. | A | `brew` |
| [profanity](https://profanity-im.github.io/) | Konsol XMPP istemcisi. | A | `pacman` |
| [senpai](https://git.sr.ht/~delthas/senpai) | Modern IRC istemcisi. | A | `pacman` |
| [signal-cli](https://github.com/AsamK/signal-cli) | Signal için resmi olmayan komut satırı istemcisi. | D | `manual` |
| [slack-term](https://github.com/erroneousboat/slack-term) | Slack terminal istemcisi. | D | `manual` |
| [tiny](https://github.com/osa1/tiny) | Rust IRC istemcisi. | A | `pacman` |
| [toot](https://github.com/ihabunek/toot) | Mastodon CLI istemcisi. | A | `pacman` |
| [tut](https://github.com/RasmusLindroth/tut) | Mastodon için TUI istemcisi. | A | `brew` |
| [urlscan](https://github.com/firecat53/urlscan) | Mutt ve terminal için URL seçici. | A | `pacman` |
| [WeeChat](https://weechat.org/) | Hafif ve genişletilebilir IRC / sohbet istemcisi. | A | `apt` |

<a id="productivity"></a>

### Verimlilik

Terminal multiplexers, notes, backup, and workflow helpers.

| App | Description | Trust | Install |
|-----|-------------|:-----:|---------|
| [Atuin](https://atuin.sh/) | Senkronize, aranabilir kabuk geçmişi. | A | `brew` |
| [autojump](https://github.com/wting/autojump) | Dizin atlama (öğrenen cd). | A | `pacman` |
| [bagels](https://github.com/EnhancedJax/Bagels) | Terminal gider / bütçe takip TUI'si. | A | `brew` |
| [borg](https://www.borgbackup.org/) | Tekilleştirmeli, sıkıştırmalı ve şifreli yedekleme (BorgBackup). | A | `pacman` |
| [calcure](https://github.com/anufrievroman/calcure) | Modern TUI takvim ve görev uygulaması. | A | `brew` |
| [calcurse](https://calcurse.org/) | Takvim ve yapılacaklar için metin arayüzü. | A | `apt` |
| [cheat](https://github.com/cheat/cheat) | Etkileşimli cheatsheet. | A | `pacman` |
| [chezmoi](https://www.chezmoi.io/) | chezmoi, dotfile ve kişisel ayarları birden fazla makinede güvenli yöneten tek ikili araçtır. Şablonlar, parola yöneticisi entegrasyonu, age/gpg ile şifreleme, arşivden içe aktarma ve kurulum betikleri sunar. Yeni makinede init+apply; chezmoi update ile güncelleme. Nova yapılandırma senkronu değildir; chezmoi ev dizininizi git deposundan uygular. | A | `pacman` |
| [fasd](https://github.com/clvv/fasd) | Sık kullanılan dosya/dizin erişimi. | A | `pacman` |
| [Glow](https://github.com/charmbracelet/glow) | Terminalde Markdown okuyucu. | A | `brew` |
| [gum](https://github.com/charmbracelet/gum) | Kabuk betikleri için güzel etkileşimli istemler. | A | `brew` |
| [howdoi](https://github.com/gleitz/howdoi) | Kod sorularına anında cevap. | C | `pipx` |
| [khal](https://lostpackets.de/khal/) | CalDAV tabanlı komut satırı takvim uygulaması. | A | `pacman` |
| [khard](https://github.com/lucc/khard) | CardDAV / vCard konsol adres defteri yöneticisi. | A | `pacman` |
| [mcfly](https://github.com/cantino/mcfly) | Akıllı kabuk geçmişi araması. | A | `pacman` |
| [navi](https://github.com/denisidoro/navi) | Etkileşimli cheatsheet aracı. | C | `cargo` |
| [psmux](https://github.com/psmux/psmux) | [Windows] PowerShell/Windows Terminal için yerel tmux uyumlu çoğullayıcı. | C | `cargo` |
| [restic](https://restic.net/) | Hızlı, güvenli ve verimli yedekleme aracı. | A | `pacman` |
| [screen](https://www.gnu.org/software/screen/) | GNU Screen — klasik terminal çoğullayıcı. | A | `pacman` |
| [slides](https://github.com/maaslalani/slides) | Markdown ile terminal sunumları. | A | `brew` |
| [Starship](https://starship.rs/) | Hızlı, özelleştirilebilir kabuk istemi. | A | `brew` |
| [taskwarrior-tui](https://github.com/kdheepak/taskwarrior-tui) | Taskwarrior için terminal kullanıcı arayüzü. | A | `pacman` |
| [thefuck](https://github.com/nvbn/thefuck) | Yanlış komutu düzeltme sihirbazı. | A | `pacman` |
| [tldr-tealdeer](https://github.com/tealdeer-rs/tealdeer) | Hızlı tldr istemcisi (tealdeer). | A | `pacman` |
| [tmux](https://github.com/tmux/tmux) | Terminal çoğullayıcı; oturum, pencere ve panel yönetimi. | A | `apt` |
| [todoman](https://github.com/pimutils/todoman) | Standartlara dayalı basit CLI görev yöneticisi. | A | `pacman` |
| [vdirsyncer](https://github.com/pimutils/vdirsyncer) | CalDAV ve CardDAV senkronizasyon aracı. | A | `pacman` |
| [wtfutil](https://wtfutil.com/) | Kişisel bilgi panosu; widget'larla terminal dashboard. | A | `brew` |
| [yadm](https://github.com/yadm-dev/yadm) | Yet Another Dotfiles Manager. | A | `pacman` |
| [zellij](https://zellij.dev/) | Kullanıcı dostu terminal çalışma alanı / çoğullayıcı. | C | `cargo` |
| [zoxide](https://github.com/ajeetdsouza/zoxide) | Akıllı cd; sık kullanılan dizinlere hızlı atlar. | A | `apt` |

<a id="games"></a>

### Oyunlar

Terminal games and playful diversions.

| App | Description | Trust | Install |
|-----|-------------|:-----:|---------|
| [2048](https://github.com/tiehuis/2048-cli) | 2048 terminal oyunu. | A | `pacman` |
| [2048-cli](https://github.com/tiehuis/2048-cli) | Terminalde 2048 oyunu. | A | `apt` |
| [Angband](https://rephial.org/) | Roguelike zindan keşfi. | A | `pacman` |
| [asciiquarium](https://robobunny.com/projects/asciiquarium/html/) | ASCII akvaryum ekran koruyucusu. | A | `apt` |
| [bastet](https://fph.altervista.org/prog/bastet.html) | Terminal Tetris (bastard tetris). | A | `apt` |
| [bsdgames](https://github.com/vattam/BSDGames) | Klasik BSD terminal oyunları seti. | A | `pacman` |
| [cbonsai](https://gitlab.com/jallbrit/cbonsai) | Terminalde büyüyen bonsai ağacı. | A | `pacman` |
| [chess-tui](https://github.com/thomas-daniels/chess-tui) | Terminal satranç arayüzü. | C | `cargo` |
| [cmatrix](https://github.com/abishekvashok/cmatrix) | Matrix yağmuru ekran efekti. | A | `apt` |
| [cowsay](https://github.com/tnalpgge/rank-amateur-cowsay) | Konuşan inek ASCII sanatı. | A | `pacman` |
| [Dungeon Crawl Stone Soup](https://crawl.develz.org/) | Roguelike macera (crawl). | A | `pacman` |
| [fortune](https://www.ibiblio.org/pub/linux/games/amusements/fortune/) | Rastgele özlü sözler. | A | `pacman` |
| [Greed](https://www.catb.org/~esr/greed/) | Sayı yiyen terminal oyunu. | A | `pacman` |
| [lolcat](https://github.com/busyloop/lolcat) | Gökkuşağı renkli cat. | A | `pacman` |
| [minesweep](https://github.com/cpcloud/minesweep-rs) | Rust mayın tarlası TUI. | C | `cargo` |
| [moon-buggy](https://github.com/k-takata/moon-buggy) | Ay aracı engel oyunu. | A | `pacman` |
| [NetHack](https://www.nethack.org/) | Klasik roguelike zindan oyunu. | A | `apt` |
| [ninvaders](https://ninvaders.sourceforge.net/) | Space Invaders klonu (ncurses). | A | `pacman` |
| [nsnake](https://github.com/alexdantas/nSnake) | Terminal yılan oyunu. | A | `apt` |
| [nudoku](https://github.com/jubalh/nudoku) | ncurses tabanlı Sudoku oyunu. | A | `brew` |
| [pacman4console](https://github.com/ebuchman/pacman-console) | Konsol Pac-Man. | A | `pacman` |
| [robotfindskitten](https://robotfindskitten.org/) | robotfindskitten zen oyunu. | A | `pacman` |
| [sl](https://github.com/mtoyoda/sl) | ls yazım hatası için buharlı tren. | A | `pacman` |
| [tetris](https://github.com/vattam/BSDGames) | BSD tetris (bsd-games). | A | `pacman` |
| [ttysolitaire](https://github.com/mpereira/tty-solitaire) | Terminal solitaire. | A | `pacman` |
| [typespeed](https://typespeed.sourceforge.net/) | Yazma hızı yarışı. | A | `pacman` |

<a id="screensavers"></a>

### Ekran Koruyucular

ASCII / terminal screensaver animations.

| App | Description | Trust | Install |
|-----|-------------|:-----:|---------|
| [asciimatics](https://github.com/peterbrittain/asciimatics) | ASCII animasyon kütüphanesi demo. | C | `pipx` |
| [astroterm](https://github.com/da-luce/astroterm) | Terminal için planetaryum / gökyüzü görüntüleyici. | A | `pacman` |
| [bonsai.sh](https://gitlab.com/jallbrit/cbonsai) | Kabuk ile bonsai ağacı. | D | `manual` |
| [lavat](https://github.com/AngelJumbo/lavat) | Lava lamba ASCII animasyonu. | D | `manual` |
| [nyancat](https://github.com/klange/nyancat) | Nyan Cat terminal animasyonu. | A | `pacman` |
| [pipes.sh](https://github.com/pipeseroni/pipes.sh) | Rastgele boru ekran koruyucusu. | A | `pacman` |
| [rusty-rain](https://github.com/cowboy8625/rusty-rain) | Rust Matrix yağmuru. | C | `cargo` |
| [termframe](https://github.com/pamburus/termframe) | Terminal ekran kaydı / çerçeve aracı. | C | `cargo` |
| [terminal-parrot](https://github.com/jmhobbs/terminal-parrot) | Dans eden papağan animasyonu. | A | `pacman` |
| [tty-clock](https://github.com/xorg62/tty-clock) | Terminalde dijital saat ekran koruyucusu. | A | `brew` |
| [unimatrix](https://github.com/will8211/unimatrix) | Unicode Matrix yağmuru. | D | `manual` |

<a id="web"></a>

### Web

Text-mode browsers and web fetch helpers.

| App | Description | Trust | Install |
|-----|-------------|:-----:|---------|
| [browsh](https://www.brow.sh/) | Modern web'i terminalde gösteren tarayıcı. | A | `brew` |
| [buku](https://github.com/jarun/buku) | Terminal yer imi yöneticisi. | A | `pacman` |
| [bulletty](https://github.com/CrociDB/bulletty) | Makaleleri Markdown olarak saklayan terminal besleme okuyucu. | A | `pacman` |
| [chafa](https://hpjansson.org/chafa/) | Terminalde görüntü gösterici (ASCII/ANSI). | A | `apt` |
| [chawan](https://git.sr.ht/~bptato/chawan) | Modern terminal web tarayıcı. | A | `pacman` |
| [ddgr](https://github.com/jarun/ddgr) | DuckDuckGo komut satırı arama aracı. | A | `apt` |
| [elinks](https://github.com/rkd77/elinks) | Gelişmiş metin web tarayıcı. | A | `pacman` |
| [googler](https://github.com/jarun/googler) | Google arama CLI (bakımda). | A | `pacman` |
| [links](https://github.com/twibright-links/links) | Metin web tarayıcı. | A | `pacman` |
| [Lynx](https://lynx.invisible-island.net/) | Klasik metin kipinde web tarayıcı. | A | `apt` |
| [newsboat](https://newsboat.org/) | RSS/Atom besleme okuyucusu. | A | `apt` |
| [w3m](https://github.com/tats/w3m) | Metin tabanlı web tarayıcı. | A | `apt` |

<a id="daily"></a>

### Günlük

Everyday utilities and general-purpose CLIs.

| App | Description | Trust | Install |
|-----|-------------|:-----:|---------|
| [arttime](https://github.com/poetaman/arttime) | ASCII sanat + saat/zamanlayıcı. | D | `manual` |
| [asciinema](https://asciinema.org/) | Terminal oturumu kaydı. | A | `pacman` |
| [bluetui](https://github.com/pythops/bluetui) | Bluetooth cihazlarını yönetmek için TUI. | A | `pacman` |
| [bluetuith](https://github.com/darkhz/bluetuith) | Bluetooth yöneticisi TUI. | A | `pacman` |
| [choose](https://github.com/theryangeary/choose) | İnsan dostu cut/awk alternatifi. | C | `cargo` |
| [csvlens](https://github.com/YS-L/csvlens) | CSV görüntüleyici TUI. | C | `cargo` |
| [dict](https://sourceforge.net/projects/dict/) | DICTd sözlük istemcisi. | A | `pacman` |
| [diskonaut](https://github.com/imsnif/diskonaut) | Disk alanı terminal haritası. | A | `pacman` |
| [dua](https://github.com/Byron/dua-cli) | Disk kullanım analizcisi (etkileşimli). | A | `pacman` |
| [entr](https://eradman.com/entrproject/) | Dosya değişince komut çalıştır. | A | `pacman` |
| [erdtree](https://github.com/solidiquis/erdtree) | Modern tree + disk kullanımı. | A | `pacman` |
| [exiftool](https://exiftool.org/) | Meta veri okuma/yazma. | A | `pacman` |
| [figlet](https://www.figlet.org/) | ASCII banner üretici. | A | `pacman` |
| [GNU Parallel](https://www.gnu.org/software/parallel/) | İşleri paralel çalıştıran kabuk aracı. | A | `pacman` |
| [hledger](https://hledger.org/) | Hafif muhasebe (Haskell ledger). | A | `pacman` |
| [ImageMagick](https://imagemagick.org/) | Görüntü dönüştürme (magick/convert). | A | `pacman` |
| [img2txt](https://caca.zoy.org/) | Görüntüyü ASCII'ye çevir (libcaca). | A | `pacman` |
| [impala](https://github.com/pythops/impala) | Wi-Fi TUI (iwd). | A | `pacman` |
| [jq](https://github.com/jqlang/jq) | JSON sorgulama ve biçimlendirme aracı. | A | `apt` |
| [jrnl](https://jrnl.sh/) | Komut satırı günlük/journal. | C | `pipx` |
| [ledger](https://www.ledger-cli.org/) | Çift taraflı muhasebe CLI. | A | `pacman` |
| [lnav](https://lnav.org/) | Gelişmiş günlük dosyası görüntüleyici. | A | `pacman` |
| [mediainfo](https://mediaarea.net/MediaInfo) | Medya dosyası teknik bilgisi. | A | `pacman` |
| [miller](https://miller.readthedocs.io/) | İsim indeksli CSV/JSON/veri işleme (mlr). | A | `pacman` |
| [moreutils](https://joeyh.name/code/moreutils/) | Unix araç kutusu (sponge, ts, parallel...). | A | `pacman` |
| [multitail](https://www.vanheusden.com/multitail/) | Çoklu günlük kuyruğu. | A | `pacman` |
| [nb](https://xwmx.github.io/nb/) | Terminal not defteri ve bilgi tabanı. | A | `pacman` |
| [netscanner](https://github.com/Chleba/netscanner) | Ağ tarama TUI. | C | `cargo` |
| [pandoc](https://pandoc.org/) | Evrensel belge dönüştürücü. | A | `apt` |
| [pdftotext](https://poppler.freedesktop.org/) | PDF araçları (poppler). | A | `pacman` |
| [progress](https://github.com/Xfennec/progress) | cp/mv/dd ilerleme durumu (eski ad: cv). | A | `pacman` |
| [pv](https://www.ivarch.com/programs/pv.shtml) | Pipe Viewer — boru hattı ilerlemesi. | A | `pacman` |
| [qpdf](https://github.com/qpdf/qpdf) | PDF dönüştürme ve onarım. | A | `pacman` |
| [qsv](https://github.com/dathere/qsv) | CSV/tabular veri işleme araç seti (xsv çatalı). | A | `pacman` |
| [remind](https://dianne.skoll.ca/projects/remind/) | Gelişmiş takvim ve alarm / hatırlatma programı. | A | `pacman` |
| [rsync](https://rsync.samba.org/) | Hızlı dosya senkronizasyon ve yedekleme aracı. | A | `apt` |
| [sc-im](https://github.com/andmarti1424/sc-im) | Terminal elektronik tablo (sc iyileştirmesi). | A | `pacman` |
| [sd](https://github.com/chmln/sd) | Sezgisel find & replace; sed alternatifi. | C | `cargo` |
| [skate](https://github.com/charmbracelet/skate) | Kişisel anahtar-değer deposu (Charm). | A | `pacman` |
| [sox](https://sourceforge.net/projects/sox/) | Ses işleme İsviçre çakısı. | A | `pacman` |
| [tabiew](https://github.com/shshemi/tabiew) | CSV dosyalarını görüntülemek ve sorgulamak için hafif TUI. | A | `pacman` |
| [taskwarrior](https://taskwarrior.org/) | Güçlü görev yöneticisi (task). | A | `pacman` |
| [tickrs](https://github.com/tarkah/tickrs) | Borsa ticker TUI. | C | `cargo` |
| [timew](https://timewarrior.net/) | Zaman takibi (Timewarrior). | A | `pacman` |
| [tldr](https://github.com/tldr-pages/tldr) | Komutların kısa ve örnekli kullanım özetlerini gösterir. | A | `apt` |
| [todo.sh](https://github.com/todotxt/todo.txt-cli) | todo.txt basit görev listesi. | A | `pacman` |
| [toilet](https://github.com/cacalabs/toilet) | Renkli ASCII banner (figlet benzeri). | A | `pacman` |
| [trans](https://github.com/soimort/translate-shell) | Google Translate CLI (translate-shell). | A | `pacman` |
| [tree](https://oldmanprogrammer.net/source.php?dir=projects/tree) | Dizin yapısını ağaç olarak listeler. | A | `apt` |
| [ttygif](https://github.com/icholy/ttygif) | ttyrec → GIF dönüştürücü. | A | `pacman` |
| [unzip](https://infozip.sourceforge.net/UnZip.html) | ZIP arşivlerini açma aracı. | A | `apt` |
| [vhs](https://github.com/charmbracelet/vhs) | Charmbracelet terminal GIF kaydı. | A | `pacman` |
| [visiData](https://www.visidata.org/) | Tablo verisi keşif TUI (vd). | A | `pacman` |
| [watson](https://github.com/TailorDev/Watson) | Zarif zaman takip CLI. | C | `pipx` |
| [when](https://github.com/bcg/when) | Basit komut satırı kişisel takvim aracı. | A | `pacman` |
| [wordgrinder](https://cowlark.com/wordgrinder/) | Terminal kelime işlemci. | A | `pacman` |
| [xsv](https://github.com/BurntSushi/xsv) | Hızlı CSV komut satırı araç seti. | C | `cargo` |
| [yq](https://github.com/mikefarah/yq) | YAML, JSON ve TOML sorgulama ve dönüştürme aracı. | A | `brew` |
| [zk](https://github.com/zk-org/zk) | Zettelkasten not CLI. | A | `pacman` |

